import datetime


class period:
    def __init__(self, name, start, end):
        if not(isinstance(start, datetime.date)):
            raise TypeError('Start must be of type datetime.date')
        self.start = start

        if not(isinstance(end, datetime.date)):
            raise TypeError('End must be of type datetime.date')
        self.end = end

        self.name = name
