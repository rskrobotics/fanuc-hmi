from bs4 import BeautifulSoup

from src.domain.numeric_register import NumericRegister


def parse_html_content_onto_numeric_registers(
    html_content: str,
) -> list[NumericRegister]:
    soup = BeautifulSoup(html_content, "html.parser")
    registers: list[NumericRegister] = []

    for row in soup.find_all("tr")[1:]:
        cols = row.find_all("td")
        if len(cols) != 3:
            continue

        identifier_text = cols[0].get_text(strip=True)
        identifier = int(identifier_text.strip("R[]"))

        comment_input = cols[1].find(
            "input", {"name": lambda x: x and x.startswith("strComment")}
        )
        comment = comment_input["value"] if comment_input else ""

        value_input = cols[2].find(
            "input",
            {"name": lambda x: x and (x.startswith("iVal") or x.startswith("rVal"))},
        )
        try:
            value = float(value_input["value"]) if value_input else 0.0
        except ValueError:
            value = 0.0

        registers.append(NumericRegister(identifier, value, comment))

    return registers
