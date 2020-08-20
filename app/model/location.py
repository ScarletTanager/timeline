# Location - defines a timeline location.  This may be a political (city, state)
# or physical (mountain range) location.  Locations also can have hierarchy/parentage -
# meaning that a location can be contained by another (e.g. a city within a state),
# which is represented by a child-parent relationship.  The parent contains the child.

class location:
    def __init__(self, name, parent=None):
        if parent is not None and not isinstance(parent, location):
            raise TypeError(
                'Argument must be of type location (or a subclass)')
        self.name = name
        self.parent = parent

    def get_parent(self):
        return self.parent
