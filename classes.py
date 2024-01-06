from dataclasses import dataclass

from soc import Period

A_GO = (1, 10)
B_GO = (11, 20)
C_GO = (21, 30)
D_GO = (31, 40)
E_GO = (1, 10)
F_GO = (11, 20)
EF_GO = (1, 20)
G_GO = (21, 30)
H_GO = (31, 40)
GH_GO = (21, 40)


@dataclass
class Class:
    name: str
    m_day: bool
    period: Period
    location: str
    go: tuple[int, int] | None = None
    category: str = "Class"
    end_period: Period | None = None
