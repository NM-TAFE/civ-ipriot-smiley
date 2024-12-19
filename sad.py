from smiley import Smiley
class Sad(Smiley):
    def __init__(self):
        super().__init__(complexion=self.BLUE)  # Pass the blue complexion to the superclass
        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self):
        """Blank out pixels to draw the sad mouth."""
        mouth = [49, 54, 42, 43, 44, 45]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        """Draw open or closed eyes."""
        eyes = [10, 13, 18, 21]
        color = self.complexion()
        for pixel in eyes:
            self.pixels[pixel] = self.BLANK if wide_open else color

    def show(self):
        """
        Show the smiley on the screen.
        """
        self.sense_hat.set_pixels(self.pixels)
