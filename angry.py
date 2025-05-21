import time
from blinkable import Blinkable
from smiley import Smiley


class Angry(Smiley, Blinkable):
    """
    Provides Smiley with angry face.
    """
    def __init__(self):
        super().__init__(complexion=self.RED)

        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self):
        """
        Draws mouth on face.
        """
        mouth = [49, 54, 42, 43, 44, 45]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        """
        Draws squinting angry eyes
        """
        eyes = [17, 22, 26, 29]
        for pixel in eyes:
            if wide_open:
                eyes = self.BLANK
            else:
                eyes = self.my_complexion
            self.pixels[pixel] = eyes

    def blink(self, delay=0.15):
        """
        Blinks and closes eyes faster
        """
        self.draw_eyes(wide_open=False)
        self.show()
        time.sleep(delay)
        self.draw_eyes(wide_open=True)
        self.show()