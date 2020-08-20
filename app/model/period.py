import datetime


class period:
    def __init__(self, name, start=datetime.date(datetime.MINYEAR, 1, 1), end=datetime.today()):
        if start != None:
            if not(isinstance(start, datetime.date)):
                raise TypeError('Start must be of type datetime.date')
            self.start = start
        else:
            self.start = datetime.date(datetime.MINYEAR, 1, 1)

        if end != None:
            if not(isinstance(end, datetime.date)):
                raise TypeError('End must be of type datetime.date')
            self.end = end
        else:
            self.end = datetime.today()

        self.name = name
