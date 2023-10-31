from dataclasses import dataclass
from datetime import time

import pytz.reference

TZ = pytz.timezone('America/Denver')


@dataclass(unsafe_hash=True)
class Period:
    name: str


class Periods:
    C1 = Period("1")
    C2 = Period("2")
    C3 = Period("3")
    C4 = Period("4")
    C5 = Period("5")
    C6 = Period("6")
    C7 = Period("7")
    PE1 = Period("1PE")
    PE3 = Period("3PE")
    PE6 = Period("6PE")


normal_soc = {
    Periods.C1: (time(7, 30, tzinfo=TZ), time(8, 23, tzinfo=TZ)),
    Periods.C2: (time(8, 30, tzinfo=TZ), time(9, 23, tzinfo=TZ)),
    Periods.C3: (time(9, 30, tzinfo=TZ), time(10, 23, tzinfo=TZ)),
    Periods.C4: (time(10, 30, tzinfo=TZ), time(11, 23, tzinfo=TZ)),
    Periods.C5: (time(12, 45, tzinfo=TZ), time(13, 38, tzinfo=TZ)),
    Periods.C6: (time(13, 45, tzinfo=TZ), time(14, 38, tzinfo=TZ)),
    Periods.C7: (time(14, 45, tzinfo=TZ), time(15, 38, tzinfo=TZ)),

    Periods.PE1: (time(7, 45, tzinfo=TZ), time(9, 0, tzinfo=TZ)),
    Periods.PE3: (time(9, 45, tzinfo=TZ), time(11, 0, tzinfo=TZ)),
    Periods.PE6: (time(14, 0, tzinfo=TZ), time(15, 15, tzinfo=TZ)),
}

special_soc_ecdt = {
    Periods.C1: (time(7, 30, tzinfo=TZ), time(8, 20, tzinfo=TZ)),
    Periods.C2: (time(8, 27, tzinfo=TZ), time(9, 17, tzinfo=TZ)),
    Periods.C3: (time(9, 24, tzinfo=TZ), time(10, 14, tzinfo=TZ)),
    Periods.C4: (time(10, 21, tzinfo=TZ), time(11, 11, tzinfo=TZ)),
    Periods.C5: (time(13, 22, tzinfo=TZ), time(14, 12, tzinfo=TZ)),
    Periods.C6: (time(14, 19, tzinfo=TZ), time(15, 9, tzinfo=TZ)),
    Periods.C7: (time(15, 16, tzinfo=TZ), time(16, 6, tzinfo=TZ)),

    Periods.PE1: (time(7, 45, tzinfo=TZ), time(8, 54, tzinfo=TZ)),
    Periods.PE3: (time(9, 39, tzinfo=TZ), time(10, 48, tzinfo=TZ)),
    Periods.PE6: (time(14, 34, tzinfo=TZ), time(15, 43, tzinfo=TZ)),
}

special_soc_parents_weekend_friday = {
    Periods.C1: (time(7, 00, tzinfo=TZ), time(7, 43, tzinfo=TZ)),
    Periods.C2: (time(7, 50, tzinfo=TZ), time(8, 33, tzinfo=TZ)),
    Periods.C3: (time(8, 40, tzinfo=TZ), time(9, 23, tzinfo=TZ)),
    Periods.C4: (time(9, 30, tzinfo=TZ), time(10, 13, tzinfo=TZ)),
    Periods.C5: None,
    Periods.C6: (time(10, 20, tzinfo=TZ), time(11, 3, tzinfo=TZ)),
    Periods.C7: (time(11, 10, tzinfo=TZ), time(11, 53, tzinfo=TZ)),

    Periods.PE1: (time(7, 10, tzinfo=TZ), time(8, 19, tzinfo=TZ)),
    Periods.PE3: (time(8, 50, tzinfo=TZ), time(9, 59, tzinfo=TZ)),
    Periods.PE6: (time(10, 30, tzinfo=TZ), time(11, 39, tzinfo=TZ)),
}
