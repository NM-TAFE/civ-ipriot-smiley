from sense_hat import SenseHat


class Smiley:
    YELLOW = (255, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    BLANK = (0, 0, 0)

    def __init__(self, complexion=None):
        self.my_complexion = complexion or self.YELLOW  # Default to yellow if no color is provided
        blank = self.BLANK
        colour = self.my_complexion
        # replaced y with colour and O with blank for readability
        self.pixels = [
            blank, colour, colour, colour, colour, colour, colour, blank,
            colour, colour, colour, colour, colour, colour, colour, colour,
            colour, colour, colour, colour, colour, colour, colour, colour,
            colour, colour, colour, colour, colour, colour, colour, colour,
            colour, colour, colour, colour, colour, colour, colour, colour,
            colour, colour, colour, colour, colour, colour, colour, colour,
            colour, colour, colour, colour, colour, colour, colour, colour,
            blank, colour, colour, colour, colour, colour, colour, blank,
        ]
        self.sense_hat = SenseHat()  # Assuming mock or real SenseHat is available

    def complexion(self):
        """Return the complexion (color) of the smiley."""
        return self.my_complexion

    def show(self):
        """Updates the pixels on the SenseHat (mock or real)."""
        self.sense_hat.set_pixels(self.pixels)
