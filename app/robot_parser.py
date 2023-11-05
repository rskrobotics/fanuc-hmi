from bs4 import BeautifulSoup
from dataclasses import dataclass
from 

@dataclass
class StringRegister:
    identifier: str
    value: str
    comment: str

def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    registers = []

    # Assuming there's a unique identifier for the table, e.g., a specific 'bordercolor'
    table = soup.find('table', {'bordercolor': '#FFFF00'})

    if not table:
        return registers
    
    rows = table.find_all('tr')[1:]  # Skip header row
    
    for row in rows:
        cells = row.find_all('td')
        identifier = cells[0].get_text(strip=True)
        comment_input = cells[1].find('input')
        value_input = cells[2].find('input')
        
        comment = comment_input['value'] if comment_input else ''
        value = value_input['value'] if value_input else ''
        
        register = StringRegister(identifier=identifier, value=value, comment=comment)
        registers.append(register)
    
    return registers

if __name__ == "__main__":
    # File path for the HTML content
    file_path = 'path/to/your/registers.html'
    
    # Read the HTML file content
    with open(file_path, 'r', encoding='iso-8859-1') as file:
        html_content = file.read()

    # Parse the HTML content
    registers = parse_html(html_content)

    # Example: Print out the parsed registers
    for register in registers:
        print(register)
