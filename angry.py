from smiley import Smiley
import time



class Angry(Smiley):
    def __init__(self):
        super().__init__(complexion = self.RED)

        Y = self.complexion()
        O = self.BLANK
        self.pixels = [
            O, Y, Y, Y, Y, Y, Y, O,
            Y, Y, Y, Y, Y, Y, Y, Y,
            Y, Y, Y, Y, Y, Y, Y, Y,
            Y, Y, Y, Y, Y, Y, Y, Y,
            Y, Y, Y, Y, Y, Y, Y, Y,
            Y, Y, Y, Y, Y, Y, Y, Y,
            Y, Y, Y, Y, Y, Y, Y, Y,
            O, Y, Y, Y, Y, Y, Y, O,
        ]

        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self):
        """
        Draws the mouth feature on a smiley
        """
        mouth = [50, 42, 43, 44, 45, 53]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        """
        Draws open or closed eyes on a smiley
        :param wide_open: Render eyes wide open or shut
        """
        eyes = [9, 10, 13, 14, 18, 21]
        for pixel in eyes:
            if wide_open:
                eyes = self.BLANK
            else:
                eyes = self.complexion()
            self.pixels[pixel] = eyes

    def blink(self, delay=0.25):

        self.draw_eyes(wide_open=False)
        self.show()
        time.sleep(delay)
        self.draw_eyes(wide_open=True)
        self.show()
