from dataclasses import dataclass


@dataclass
class NumericRegister:
    id: int
    value: float
    comment: str
