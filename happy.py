import contextlib
import time

import pyttsx3

from blinkable import Blinkable
from smiley import Smiley, TTSStream


class Happy(Smiley, Blinkable):
    """
    Provides a Smiley with a happy expression.

    For accessibility the class prints to the standard output the state of the "happy" smiley.
    """

    def __init__(self):
        super().__init__()
        self.engine = pyttsx3.init()
        self.tts_stream = TTSStream(self.engine)
        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self):
        """
        Renders a mouth by blanking the pixels that form that object.
        """
        description = f"Drawing a YELLOW {self.mood} face: {self.emoji}"

        with contextlib.redirect_stdout(self.tts_stream), contextlib.redirect_stderr(self.tts_stream):
            print(description)

        mouth = [41, 46, 50, 51, 52, 53]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        """
        Draws the eyes (open or closed) on the standard smiley.

        For accessibility: describes state of smiley eyes to user

        :param wide_open (bool): eyes open or closed.
        """
        description = f"{self.mood} eyes open"
        if not wide_open:
            description = f"{self.mood} eyes closed"

        with contextlib.redirect_stdout(self.tts_stream), contextlib.redirect_stderr(self.tts_stream):
            print(description)

        eyes = [10, 13, 18, 21]
        for pixel in eyes:
            self.pixels[pixel] = self.BLANK
            if not wide_open:
                self.pixels[pixel] = self.YELLOW

    def blink(self, delay=0.25):
        """
        Blinks the smiley's eyes once

        For accessibility: describes state of smiley blink to user

        :param delay: Delay between blinks (in seconds)
        """
        description = "Blink Started"
        with contextlib.redirect_stdout(self.tts_stream), contextlib.redirect_stderr(self.tts_stream):
            print(description)

        self.draw_eyes(wide_open=False)
        self.show()

        time.sleep(delay)

        self.draw_eyes(wide_open=True)
        self.show()

        description = "Blink Completed"
        with contextlib.redirect_stdout(self.tts_stream), contextlib.redirect_stderr(self.tts_stream):
            print(description)
