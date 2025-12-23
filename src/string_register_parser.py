from bs4 import BeautifulSoup

from src.domain.string_register import StringRegister


def parse_html_content_onto_string_registers(html_content: str) -> list[StringRegister]:
    soup = BeautifulSoup(html_content, "html.parser")
    registers: list[StringRegister] = []

    for row in soup.find_all("tr")[1:]:
        cols = row.find_all("td")
        if len(cols) != 3:
            continue

        identifier_text = cols[0].get_text(strip=True)
        identifier = int(identifier_text.strip("SR[]"))

        comment_input = cols[1].find(
            "input", {"name": lambda x: x and x.startswith("strComment")}
        )
        comment = comment_input["value"] if comment_input else ""

        value_input = cols[2].find(
            "input", {"name": lambda x: x and x.startswith("iVal")}
        )
        value = value_input["value"] if value_input else ""

        registers.append(StringRegister(identifier, value, comment))

    return registers
