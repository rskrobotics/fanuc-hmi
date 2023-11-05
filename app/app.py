from datetime import datetime
from flask import Flask, render_template, jsonify, request
from apscheduler.schedulers.background import BackgroundScheduler
from flask_caching import Cache
import requests
from robot_service import RobotService
from config_service import ConfigService

app = Flask(__name__)
config_service = ConfigService()
robot_service = RobotService(ip_address=config_service.get('robot.ip'))


scheduler = BackgroundScheduler()
scheduler.add_job(func=robot_service.fetch_numeric_registers,
                  trigger='interval', seconds=config_service.get('fetch_intervals.seconds_numeric'))

scheduler.add_job(
    func=robot_service.fetch_string_registers,
    trigger='interval',
    seconds=config_service.get('fetch_intervals.seconds_string'),
    next_run_time=datetime.now()
)

cache_timeout = config_service.get('cache_timeout_seconds', 3600)
app.config['CACHE_TYPE'] = 'SimpleCache'
app.config['CACHE_DEFAULT_TIMEOUT'] = cache_timeout

cache = Cache(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/update-data')
def update_data():
    all_numeric_registers = robot_service.numeric_registers
    displayed_numeric_indices = config_service.get(
        'displayed_registers.numeric')
    numeric_registers = [
        reg for reg in all_numeric_registers if reg.id in displayed_numeric_indices]
    return render_template('numeric_registers.html', numeric_registers=numeric_registers)


@app.route('/update-message')
def update_message():
    quote_api_url = config_service.get(
        'quote_api_url', "https://api.quotable.io/random")
    message = cache.get('cached_message')
    template_color_class = 'default-color'

    if message is None:
        try:
            response = requests.get(quote_api_url)
            if response.status_code == 200:
                quote_data = response.json()
                message = quote_data.get('content')
                cache.set('cached_message', message, timeout=cache_timeout)
            else:
                message = "Default Message"
                cache.set('cached_message', message, timeout=cache_timeout)
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            message = "Default Message"
            cache.set('cached_message', message, timeout=cache_timeout)

    string_register_index = next(
        (reg.value for reg in robot_service.numeric_registers if reg.id == 31), 0
    )

    if string_register_index > 0:
        try:
            message_register = next(
                (reg for reg in robot_service.string_registers if reg.id == string_register_index), None)

            if message_register is not None:
                message = message_register.value
                template_color_class = 'register-color'
            else:
                raise ValueError(
                    f"No string register with identifier {string_register_index}")

        except ValueError as e:
            template_color_class = "error-color"
            message = str(e)
    elif string_register_index == 0:
        pass
    else:
        template_color_class = "error-color"
        message = "Invalid register index: Index should be positive."

    return render_template('message.html', message=message, template_color_class=template_color_class)


@app.route('/keypress', methods=['POST'])
def keypress():
    data = request.get_json()
    if data and data['key'] == 'z':
        print("Z key was pressed")
        robot_service.set_numeric_register_value(register_index=config_service.get(
            'trigger.register_id'), value=config_service.get('trigger.value'))
        return jsonify({"status": "success"}), 200
    else:
        print("Invalid key was pressed")
        return jsonify({"error": "Invalid key pressed"}), 400


@app.teardown_appcontext
def shutdown_scheduler(response_or_exc):
    if response_or_exc is None and scheduler.running:
        scheduler.shutdown()
    return response_or_exc


if __name__ == '__main__':
    scheduler.start()
    try:
        app.run(debug=True, host='0.0.0.0')
    except (KeyboardInterrupt, SystemExit):
        pass
    finally:
        scheduler.shutdown()
