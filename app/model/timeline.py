import period
import event
import actor


class Timeline:
    def __init__(self, name):
        self.name = name

        self.events = []
        self.actors = set()

    def add_event(self, e):
        if not(isinstance(e, event.event)):
            raise TypeError(
                'Timeline events must be of type event.event (or a subclass)')

        if e.participants - self.actors:
            raise InvalidEventError(
                'Event has participants not actors in timeline')

        self.events.append(e)

    def add_actor(self, a):
        if not(isinstance(a, actor.actor)):
            raise TypeError(
                'Timeline actors must be of type actor.actor (or a subclass)')

        self.actors.append(a)

    def has_actor(self, a):
        return a in self.actors


class InvalidEventError(Exception):
    def __init__(self, reason):
        self.reason = reason
