from collections import defaultdict
from dataclasses import dataclass
from datetime import date, time, timedelta, datetime

from ics import Event

from classes import Class
from soc import Period, TZ


@dataclass
class DaySchedule:
    date: date
    m_day: bool
    lesson: int
    soc: dict[Period, tuple[time, time]]

    def get_events(self, classes: list[Class]) -> list[Event]:
        events = []

        day_event = Event()
        day_event.name = f"{'M' if self.m_day else 'T'}{self.lesson}"
        day_event.begin = self.date
        day_event.end = self.date
        day_event.categories.add("Schedules")
        day_event.make_all_day()
        events.append(day_event)

        if self.date.weekday() <= 3:
            cyber_event = Event()
            cyber_event.name = "Cyber Practice"
            cyber_event.begin = datetime.combine(self.date, time(15, 45, tzinfo=TZ))
            cyber_event.end = datetime.combine(self.date, time(17, 0, tzinfo=TZ))
            cyber_event.categories.add("Club")
            events.append(cyber_event)

        for c in classes:
            if c.m_day != self.m_day:
                continue

            if c.go is not None and (c.go[0] > self.lesson or c.go[1] < self.lesson):
                continue

            if self.soc[c.period] is None:
                continue

            end_period = c.end_period if c.end_period else c.period
            if c.name == "MSS 251":  # CAUSE MSS IS WEIRD
                single_periods = {1, 2, 3, 7, 8, 9, 12, 13, 19, 21, 24, 25, 26, 27, 32, 40}
                if self.lesson in single_periods:
                    end_period = c.period

            e = Event()
            e.name = f"[{'M' if c.m_day else 'T'}{c.period.name}] {c.name}"
            e.begin = datetime.combine(self.date, self.soc[c.period][0])
            e.end = datetime.combine(self.date, self.soc[end_period][1])
            e.categories.add(c.category)
            e.location = c.location
            events.append(e)

        return events


@dataclass
class SemesterSchedule:
    start_date: date
    weekdays_off: set[date]
    normal_soc: dict[Period, tuple[time, time]]
    special_soc_dates: dict[date, dict[Period, tuple[time, time]]]
    days: int = 40

    def get_days(self):
        d = self.start_date
        lesson = 1
        m_day = True
        soc_dict = defaultdict(lambda: self.normal_soc, self.special_soc_dates)

        while lesson <= 40:
            yield DaySchedule(d, m_day, lesson, soc_dict[d])
            m_day = not m_day
            if m_day:
                lesson += 1
            d += timedelta(days=1)
            while d.weekday() >= 5 or d in self.weekdays_off:
                d += timedelta(days=1)
