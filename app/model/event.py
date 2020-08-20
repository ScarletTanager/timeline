# Event - represents a timeline event.

import period
import actor


class event(period):
    def __init__(self, name, start, end):
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
