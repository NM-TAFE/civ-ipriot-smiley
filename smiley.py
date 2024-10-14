import io

import pyttsx3

from sense_hat import SenseHat


class TTSStream(io.StringIO):
    def __init__(self, engine):
        super().__init__()
        self.engine = engine

    def write(self, text):
        super().write(text)
        self.engine.say(text)
        self.engine.runAndWait()


class Smiley:
    """

    For accessibility the class prints to the standard output the state of the smiley.

    ---
    Smiley Colours:
    - Defined by using Red, Green & Blue values.
    - Each may have values from 0 to 255.
    - 0 is OFF, 255 is fully on

    Other colour examples:
    - CYAN = 0 255 255
    - MAGENTA = 255 0 255
    - AMBER = 255 191 0

    References:
        - https://www.rapidtables.com/web/color/RGB_Color.html
        - https://rgbcolorcode.com
        - https://html-color.codes
    """
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    BLANK = (0, 0, 0)

    def __init__(self, mood="happy", emoji="😀"):
        # We have encapsulated the SenseHat object
        self.sense_hat = SenseHat()
        self.engine = pyttsx3.init()

        Y = self.YELLOW
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
        self.mood = mood
        self.emoji = emoji

    def dim_display(self, dimmed=True):
        """
        Set the SenseHat's light intensity to low (True) or high (False)
        :param dimmed: Dim the display if True, otherwise don't dim
        """
        self.sense_hat.low_light = dimmed

    def show(self):
        """
        Show the smiley on the screen.
        """
        self.sense_hat.set_pixels(self.pixels)
