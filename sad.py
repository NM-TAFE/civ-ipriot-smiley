from smiley import Smiley, TTSStream
import contextlib
import pyttsx3

class Sad(Smiley):
    """Challenges (repeated from smiley):
    1. Notice that all smileys inherit the mood of their parent!
    2. Make it so the mood is parameterised in both the parent and child
    3. ensure that the draw mouth correctly encapsulates the mood of the smiley
    """
    def __init__(self):
        super().__init__("sad","🙁")
        self.engine = pyttsx3.init()
        self.tts_stream = TTSStream(self.engine)
        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self):
        """
        Draws the mouth feature on a smiley
        """
        description = f"Drawing a YELLOW {self.mood} face: {self.emoji}"

        with contextlib.redirect_stdout(self.tts_stream), contextlib.redirect_stderr(self.tts_stream):
            print(description)

        mouth = [49, 54, 42, 43, 44, 45]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        """
        Draws open or closed eyes on a smiley

        For accessibility: describes state of smiley eyes to user

        :param wide_open: Render eyes wide open or shut
        """
        description = f"{self.mood} eyes open"
        if not wide_open:
            description = f"{self.mood} eyes closed"

        with contextlib.redirect_stdout(self.tts_stream), contextlib.redirect_stderr(self.tts_stream):
            print(description)

        eyes = [10, 13, 18, 21]
        for pixel in eyes:
            if wide_open:
                eyes = self.BLANK
            else:
                eyes = self.YELLOW
            self.pixels[pixel] = eyes
