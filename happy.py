import time
from blinkable import Blinkable
from smiley import Smiley


class Happy(Smiley, Blinkable):
    """
    Happy is a subclass of Smiley and of Blinkable.

    Note that Blinkable is an interface (an abstract base
    class that only contains an abstract method). By subclassing
    Blinkable, this class promises to implement the abstract
    method.See {meth:blink} below.
    """
    def __init__(self):
        super().__init__()

        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self):
        """
        Method that draws the mouth on the standard faceless smiley.
        """
        mouth = [41, 46, 50, 51, 52, 53]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        """
        Method that draws the eyes (open or closed) on the standard smiley.
        :param wide_open: True if eyes opened, False otherwise
        """
        eyes = [10, 13, 18, 21]
        for pixel in eyes:
            self.pixels[pixel] = self.BLANK if wide_open else self.complexion()

    def blink(self, delay=0.25):
        """
        Make the happy smiley blink once with a certain delay (in s).
        This is the implementation of the abstract method from the
        Blinkable abstract class.

        :param delay: Delay in seconds
        """
        self.draw_eyes(wide_open=False)
        self.show()
        time.sleep(delay)
        self.draw_eyes(wide_open=True)
        self.show()
