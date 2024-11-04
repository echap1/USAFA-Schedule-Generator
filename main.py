from datetime import date

from classes import Class, C_GO, D_GO, EF_GO, GH_GO, G_GO
from schedule import SemesterSchedule
from soc import Periods, normal_soc, special_soc_ecdt
from ics import Calendar

start_date = date(2024, 8, 8)

off_days: set[date] = {
    date(2024, 8, 30),
    date(2024, 9, 2),
    date(2024, 10, 14),
    date(2024, 10, 18),
    date(2024, 11, 11),
    date(2024, 11, 27),
    date(2024, 11, 28),
    date(2024, 11, 29),
}

ssoc_days = {
    date(2023, 8, 21): special_soc_ecdt,
    date(2023, 9, 18): special_soc_ecdt,
    date(2023, 10, 23): special_soc_ecdt,
    date(2023, 11, 13): special_soc_ecdt,

    date(2024, 1, 22): special_soc_ecdt,
    date(2024, 2, 12): special_soc_ecdt,
    date(2024, 3, 12): special_soc_ecdt,
    date(2024, 4, 23): special_soc_ecdt,
}


M_DAY = True
T_DAY = False

classes = [
    # # M Days
    # Class("Mech 220", M_DAY, Periods.C1, "Fairchild 5H20"),
    # # Class("English 211", M_DAY, Periods.C2, "Fairchild 4D10"),
    # Class("ECE 495", M_DAY, Periods.C3, "Fairchild 2F50"),
    # Class("CompSci 467", M_DAY, Periods.C4, "Fairchild 4F5"),
    # Class("TBD", M_DAY, Periods.C5, "TBD", category="Squad Meeting"),
    # Class("Physics 215", M_DAY, Periods.C6, "Fairchild 2C18", end_period=Periods.C7),
    #
    # # T Days
    # Class("MSS 251", T_DAY, Periods.C1, "Fairchild 2B8", end_period=Periods.C2),
    # # Class("Spark Period", T_DAY, Periods.C7, "Fairchild 4D45"),
    # Class("Leadership 200", T_DAY, Periods.C6, "Fairchild 5H23", C_GO),
    # Class("Swimming", T_DAY, Periods.PE3, "CFC", D_GO)

    # M Days
    Class("Cyber 333", M_DAY, Periods.C1, "Fairchild 2E11", end_period=Periods.C2),
    Class("English 212", M_DAY, Periods.C3, "Fairchild 3J11"),
    Class("Cyber 435", M_DAY, Periods.C4, "Fairchild 2D17"),
    Class("ECE 382", M_DAY, Periods.C5, "Fairchild 2E48"),
    Class("Leadership 300", M_DAY, Periods.C6, "Fairchild 5H22", go=C_GO),

    # T Days
    Class("ECE 321", T_DAY, Periods.C1, "Fairchild 2G6", end_period=Periods.C2),
    Class("ECE 346", T_DAY, Periods.C5, "Fairchild 2E35"),
]

s = SemesterSchedule(start_date, off_days, normal_soc, ssoc_days)

cal = Calendar()

for day in s.get_days():
    for event in day.get_events(classes):
        cal.events.add(event)

f = open("cal.ics", "w")
f.writelines(cal.serialize_iter())
f.close()