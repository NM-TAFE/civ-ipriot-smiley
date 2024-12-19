from smiley import Smiley
class Angry(Smiley):
    def __init__(self):
        super().__init__(complexion=self.RED)  # Red complexion for Angry
        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self):
        """Draw a fierce angry mouth."""
        mouth = [49, 54, 42, 43, 44, 45]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        """Draw fierce eyes."""
        eyes = [10, 13, 18, 21]
        color = self.complexion()
        for pixel in eyes:
            self.pixels[pixel] = self.BLANK if wide_open else color

    def show(self):
        """
        Show the smiley on the screen.
        """
        self.sense_hat.set_pixels(self.pixels)
