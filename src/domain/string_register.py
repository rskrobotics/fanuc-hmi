from dataclasses import dataclass


@dataclass
class StringRegister:
    id: int
    value: str
    comment: str
