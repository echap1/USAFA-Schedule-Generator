from datetime import date

from classes import Class, C_GO, D_GO
from schedule import SemesterSchedule
from soc import Periods, normal_soc, special_soc_ecdt, special_soc_parents_weekend_friday
from ics import Calendar

start_date = date(2023, 8, 10)

off_days: set[date] = {
    date(2023, 9, 4),  # Labor Day
    date(2023, 9, 27),  # CW Training Day
    date(2023, 10, 9),  # Columbus Day
    date(2023, 11, 10),  # Veterans Day

    date(2023, 11, 22),  # THANKSGIVING
    date(2023, 11, 23),
    date(2023, 11, 24),
    date(2023, 11, 25),
    date(2023, 11, 26)
}

ssoc_days = {
    date(2023, 8, 16): special_soc_ecdt,
    date(2023, 9, 1): special_soc_parents_weekend_friday,
    date(2023, 9, 13): special_soc_ecdt,
    date(2023, 10, 18): special_soc_ecdt,
    date(2023, 11, 15): special_soc_ecdt,
}


M_DAY = True
T_DAY = False

classes = [
    # M Days
    Class("Mech 220", M_DAY, Periods.C1, "Fairchild 5H20"),
    # Class("English 211", M_DAY, Periods.C2, "Fairchild 4D10"),
    Class("ECE 495", M_DAY, Periods.C3, "Fairchild 2F50"),
    Class("CompSci 467", M_DAY, Periods.C4, "Fairchild 4F5"),
    Class("TBD", M_DAY, Periods.C5, "TBD", category="Squad Meeting"),
    Class("Physics 215", M_DAY, Periods.C6, "Fairchild 2C18", end_period=Periods.C7),

    # T Days
    Class("MSS 251", T_DAY, Periods.C1, "Fairchild 2B8", end_period=Periods.C2),
    # Class("Spark Period", T_DAY, Periods.C7, "Fairchild 4D45"),
    Class("Leadership 200", T_DAY, Periods.C6, "Fairchild 5H23", C_GO),
    Class("Swimming", T_DAY, Periods.PE3, "CFC", D_GO)
]

s = SemesterSchedule(start_date, off_days, normal_soc, ssoc_days)

cal = Calendar()

for day in s.get_days():
    for event in day.get_events(classes):
        cal.events.add(event)

f = open("cal.ics", "w")
f.writelines(cal.serialize_iter())
f.close()
