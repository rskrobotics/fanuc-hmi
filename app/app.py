import logging
import string
import threading
import time
from datetime import datetime, timedelta
from logging.handlers import RotatingFileHandler

import requests
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, render_template, jsonify, request
from flask_caching import Cache

from config_service import ConfigService
from robot_service import RobotService

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

handler = RotatingFileHandler(
    'hmi.log', maxBytes=10000, backupCount=3
)
formatter = logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s [in %(module)s:%(lineno)d]'
)
handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)
root_logger = logging.getLogger()
root_logger.addHandler(handler)
root_logger.setLevel(logging.DEBUG)
logging.getLogger('apscheduler').setLevel(logging.WARNING)

logger = logging.getLogger(__name__)
logger.debug('This is a debug message that will go into the hmi.log file')

config_service = ConfigService()
robot_service = RobotService(ip_address=config_service.get('robot.ip'),
                             mock_data=config_service.get('mock_robot_data', True))

scheduler = BackgroundScheduler()
scheduler.add_job(func=robot_service.fetch_numeric_registers,
                  trigger='interval', seconds=config_service.get('fetch_intervals.seconds_numeric'),
                  max_instances=1
                  )

scheduler.add_job(
    func=robot_service.fetch_string_registers,
    trigger='interval',
    seconds=config_service.get('fetch_intervals.seconds_string'),
    next_run_time=datetime.now() + timedelta(seconds=8),
    max_instances=1
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
    all_numeric_registers = robot_service.get_numeric_registers()
    displayed_numeric_indices = config_service.get('displayed_registers.numeric')

    # Extract the value for register 28
    timer = next((reg for reg in all_numeric_registers if reg.id == 28), None)
    timer_value = timer.value if timer else None

    numeric_registers = [
        reg for reg in all_numeric_registers if reg.id in displayed_numeric_indices
    ]
    return render_template('content.html',
                           numeric_registers=numeric_registers,
                           timer_value=timer_value)


@app.route('/update-message')
def update_message():
    quote_api_url = config_service.get(
        'quote_api_url', "http://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json")
    message = cache.get('cached_message')
    template_color_class = 'default-color'

    if message is None:
        try:
            response = requests.get(quote_api_url)
            if response.status_code == 200:
                quote_data = response.json()
                message = quote_data.get('quoteText')
                if quote_data.get('quoteAuthor'):
                    message += f" - {quote_data.get('quoteAuthor')}"
                cache.set('cached_message', message, timeout=cache_timeout)
            else:
                message = "Default Message"
                cache.set('cached_message', message, timeout=cache_timeout)
        except requests.RequestException as e:
            logger.error(f"Request failed: {e}")
            message = "Default Message"
            cache.set('cached_message', message, timeout=cache_timeout)

    string_register_index = int(next(
        (reg.value for reg in robot_service.numeric_registers if reg.id == 31), 0
    ))

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

    if data and data['key'].lower() in string.ascii_lowercase:
        logger.info(f"{data['key']} key was pressed")
        robot_service.set_numeric_register_value(
            register_index=config_service.get('trigger.register_id'),
            value=config_service.get('trigger.value')
        )

        def reset_value():
            time.sleep(config_service.get('trigger.revert_delay_seconds'))
            robot_service.set_numeric_register_value(
                register_index=config_service.get('trigger.register_id'),
                value=config_service.get('trigger.revert_value')
            )

        # Start the background thread
        thread = threading.Thread(target=reset_value)
        thread.start()

        return jsonify({"status": "success"}), 200

    else:
        logger.warning("Invalid key was pressed")
        return jsonify({"error": "Invalid key pressed"}), 400


if __name__ == '__main__':
    scheduler.start()
    try:
        app.run(debug=True, threaded=True, host='0.0.0.0', use_reloader=False)
    except (KeyboardInterrupt, SystemExit):
        pass
    finally:
        scheduler.shutdown()
