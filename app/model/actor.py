# Actor - defines a timeline participant ("actor")
import datetime


class actor:
    def __init__(self, name):
        self.name = name


class person(actor):
    def __init__(self, name, born, died=None):
        super().__init__(name)
        if not(isinstance(born, datetime.date)):
            raise TypeError('born must be of type datetime.date')
        self.born = born

        if died != None:
            if not(isinstance(died, datetime.date)):
                raise TypeError('died must be of type datetime.date')
        self.died = died

    def is_living(self):
        return self.died is None
