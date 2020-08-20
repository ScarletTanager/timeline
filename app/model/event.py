# Event - represents a timeline event.

import period
import actor
import location
import datetime


class event(period.period):
    def __init__(self, name, start=datetime.date(datetime.MINYEAR, 1, 1), end=datetime.date.today()):
        try:
            super().__init__(name, start, end)
        except TypeError:
            raise

        self.participants = set()

    def add_participant(self, participant):
        if not(isinstance(participant, actor.actor)):
            raise TypeError(
                'Event participants must be of type actor.actor (or a subclass)')

        self.participants.add(participant)

    def set_location(self, l):
        if not(isinstance(l, location.location)):
            raise TypeError(
                'Location must be of type location.location (or a subclass)')
        self.location = l
