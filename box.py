import csv
import cv2 as cv
from unit import Unit


class Box:
    def __init__(self, player):
        self.units = []
        self.player = player

    def init_player(self, units):
        """units -- dict with key as name and def as Unit."""
        with open('resources/playerunits.csv') as f:
            r = csv.reader(f)
            for row in r:
                self.units.append(units[row[0]])

    def init_opponent(self, screenshot):
        # begin cutting AOI
        # gonna make diff class for this
        # has comparison, create dict {unit: image} func
        pass
