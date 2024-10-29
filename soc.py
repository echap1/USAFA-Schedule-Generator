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
    PE1 = Period("1PE")
    PE3 = Period("3PE")
    PE5 = Period("5PE")


normal_soc = {
    Periods.C1: (time(8, 0, tzinfo=TZ), time(8, 53, tzinfo=TZ)),
    Periods.C2: (time(9, 0, tzinfo=TZ), time(9, 53, tzinfo=TZ)),
    Periods.C3: (time(10, 0, tzinfo=TZ), time(10, 53, tzinfo=TZ)),
    Periods.C4: (time(11, 0, tzinfo=TZ), time(11, 53, tzinfo=TZ)),
    Periods.C5: (time(13, 0, tzinfo=TZ), time(13, 53, tzinfo=TZ)),
    Periods.C6: (time(14, 0, tzinfo=TZ), time(14, 53, tzinfo=TZ)),

    Periods.PE1: (time(8, 15, tzinfo=TZ), time(9, 30, tzinfo=TZ)),
    Periods.PE3: (time(10, 15, tzinfo=TZ), time(11, 30, tzinfo=TZ)),
    Periods.PE5: (time(13, 30, tzinfo=TZ), time(14, 45, tzinfo=TZ)),
}

special_soc_ecdt = {
    Periods.C1: (time(8, 0, tzinfo=TZ), time(8, 53, tzinfo=TZ)),
    Periods.C2: (time(9, 0, tzinfo=TZ), time(9, 53, tzinfo=TZ)),
    Periods.C3: (time(10, 0, tzinfo=TZ), time(10, 53, tzinfo=TZ)),
    Periods.C4: (time(11, 0, tzinfo=TZ), time(11, 53, tzinfo=TZ)),
    Periods.C5: (time(14, 0, tzinfo=TZ), time(14, 53, tzinfo=TZ)),
    Periods.C6: (time(15, 0, tzinfo=TZ), time(15, 53, tzinfo=TZ)),

    Periods.PE1: (time(8, 15, tzinfo=TZ), time(9, 30, tzinfo=TZ)),
    Periods.PE3: (time(10, 15, tzinfo=TZ), time(11, 30, tzinfo=TZ)),
    Periods.PE5: (time(14, 15, tzinfo=TZ), time(15, 30, tzinfo=TZ)),
}
