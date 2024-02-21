import numpy


class Room :
    def __init__(self, name: str, description: str, exits: numpy.ndarray, objects: numpy.ndarray, exit_locked: bool = False) :
        self.exits = exits
        self.name = name
        self.desc = description
        self.exit_locked = exit_locked

    def open_exit(self) :
        self.exit_locked = False

    def access(self, object_name: str) :
        for obj in self.objects.flat :
            if obj.name == object_name :
                return obj