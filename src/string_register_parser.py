from bs4 import BeautifulSoup

from domain.string_register import StringRegister
from mocks.mock_string_response import MockStringResponse


def parse_html_content_onto_string_registers(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    registers = []

    for row in soup.find_all('tr')[1:]:
        cols = row.find_all('td')
        if len(cols) != 3:
            continue

        identifier_text = cols[0].get_text(strip=True)
        identifier = int(identifier_text.strip('SR[]'))

        comment = cols[1].find('input', {'name': lambda x: x and x.startswith('strComment')})['value']
        value = cols[2].find('input', {'name': lambda x: x and x.startswith('iVal')})['value']

        registers.append(StringRegister(identifier, value, comment))

    return registers


if __name__ == '__main__':
    html_content = MockStringResponse
    registers = parse_html_content_onto_string_registers(html_content)

    for reg in registers:
        print(reg)
