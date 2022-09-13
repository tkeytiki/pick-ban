import cv2 as cv
from unit import Unit
import os

BOX1_X = 36     # distances from image edge to box
BOX2_X = 0      # tbd
BOX_Y = 184
BOX_W = 192
BOX_H = 317
#ICON_W = 60
#ICON_H = 61
ICON_X = 15     # distances from icon edge to crop out border
ICON_Y = 10
ICON_W = 30
ICON_H = 42
COL_D = 66      # distances between next icon crop
ROW_D = 64
COL_P = 6       # padding between cols
ROW_P = 3       # padding between rows
BOX_PATH = 'resources/tempbox.png'
UNIT_PATH = 'resources/units/'

class Image:
    @staticmethod
    def init_dict() -> dict:
        """Return a dict with key 'unit_name' and definition 'filepath'"""
        d = {}
        for file in os.listdir(UNIT_PATH):
            d[file.split(".")[0]] = cv.imread(os.path.join(UNIT_PATH, file))
        return d

    @staticmethod
    def compare(img1, img2) -> bool:
        diff = cv.subtract(img1, img2)
        b, g, r = cv.split(diff)
        if cv.countNonZero(b) == 0 and cv.countNonZero(g) == 0 and cv.countNonZero(r) == 0:
            return True
        return False

    @staticmethod
    def find_unit(crop, units) -> Unit:
        """Find a match for the unit in the cropped image
        note: search could be optimized by sorting units by dominant colour"""
        pass

    @staticmethod
    def cut_aoi(player):
        """Create crop of box from screenshot in clipboard and write to clipboard."""
        # get screenshot
        ss = cv.imread('resources/units/intheory.png')
        if player == 1:
            box_x = BOX1_X
            # player 1
        else:
            box_x = BOX2_X
            # player 2
        ss = ss[BOX_Y:BOX_Y+BOX_H, box_x:box_x+BOX_W]
        cv.imwrite(BOX_PATH, ss)

    @staticmethod
    def init_unitlist() -> list:
        """Create a list of Units in a box from cropped screenshot."""
        box = cv.imread(BOX_PATH)
        x = 0
        y = 0
        # d = Image.init_dict()
        l = []

        for i in range(5):
            for j in range(3):
                crop = box[y:y + ICON_H, x:x + ICON_W]
                cv.imshow('yes', crop)
                x = x + COL_D
                cv.waitKey(0)
                #print("enter name: \n")
                #name = input()
                #cv.imwrite(UNIT_PATH + name, crop)

            y = y + ROW_D
            x = 0
        '''for i in range(15):
            # harvest crops
            crop = 0
            l.append(Image.find_unit(crop, d))'''
        return l
