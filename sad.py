import time
from blinkable import Blinkable
from smiley import Smiley


class Sad(Smiley, Blinkable):
    def __init__(self):
        super().__init__()

        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self):
        """
        Draws the mouth feature on a smiley
        """
        mouth = [49, 54, 42, 43, 44, 45]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        """
        Draws open or closed eyes on a smiley
        :param wide_open: Render eyes wide open or shut
        """
        eyes = [10, 13, 18, 21]
        for pixel in eyes:
            if wide_open:
                eyes = self.BLANK
            else:
                eyes = self.complexion()
            self.pixels[pixel] = eyes

    def blink(self, delay=0.5):
        """
       Blinks the smiley's eyes once

        :param delay: Delay between blinks (in seconds)
        """
        while True:
            self.draw_eyes(True)
            self.show()
            time.sleep(delay)
            self.draw_eyes(False)
            self.show()
            time.sleep(0.2)
            self.draw_eyes(True)
            self.show()
            time.sleep(0.5)
            self.draw_eyes(False)
            self.show()
            time.sleep(0.2)
