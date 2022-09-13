import type as tp

class Unit:
    def __init__(self, name, factions, types, img, range, threatens, threatened_by):
        self.name = name
        self.factions = factions
        self.types = types
        self.img = img
        self.range = range
        self.threatens = threatens
        self.threatened_by = threatened_by
        self.priority = 0

    def add_prio(self, a):
        """Adds a to priority."""
        self.priority = self.priority + a
