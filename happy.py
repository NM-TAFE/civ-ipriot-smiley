from smiley import Smiley
class Happy(Smiley):
    """
    Provides a Smiley with a happy expression.
    """
    def __init__(self):
        super().__init__()  # Default color will be yellow, but can be overridden

        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self):
        """
        Renders a mouth by blanking the pixels that form that object.
        """
        mouth = [41, 46, 50, 51, 52, 53]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        """
        Draws the eyes (open or closed) on the standard smiley.
        :param wide_open (bool): eyes open or closed.
        """
        eyes = [10, 13, 18, 21]
        color = self.complexion()  # Get the complexion (color) from the superclass method
        for pixel in eyes:
            self.pixels[pixel] = self.BLANK if wide_open else color  # Use the complexion color

    def show(self):
        """
        Show the smiley on the screen.
        """
        self.sense_hat.set_pixels(self.pixels)
