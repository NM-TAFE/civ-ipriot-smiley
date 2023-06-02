from sense_hat import SenseHat


class Smiley:
    """
    A basic smiley. This base class defines the basic face shape of a smiley
    and the potential colours a smiley can be. It also handles the smiley's
    interactions with the Sense HAT.
    """
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    BLUE = (0, 0, 255)
    BLANK = (0, 0, 0)

    def __init__(self, complexion=YELLOW):
        """
        Initialise the smiley with a complexion colour and a basic face
        shape.
        :param complexion: The colour of the smiley as RGB values, represented
            as a tuple of three ints.
        """
        # We have encapsulated the SenseHat object
        self.sense_hat = SenseHat()
        self.my_complexion = complexion

        C = complexion
        O = self.BLANK
        self.pixels = [
            O, C, C, C, C, C, C, O,
            C, C, C, C, C, C, C, C,
            C, C, C, C, C, C, C, C,
            C, C, C, C, C, C, C, C,
            C, C, C, C, C, C, C, C,
            C, C, C, C, C, C, C, C,
            C, C, C, C, C, C, C, C,
            O, C, C, C, C, C, C, O,
        ]

    def complexion(self):
        """
        Get the colour to draw the smiley with.
        :returns: a tuple of ints representing the colour by RGB values
        """
        return self.my_complexion

    def dim_display(self, dimmed=True):
        """
        Set the SenseHat's light intensity to low (True) or high (False)
        :param dimmed: Dim the display if True, otherwise don't dim
        """
        self.sense_hat.low_light = dimmed

    def show(self):
        """
        Show the smiley on the Sense HAT LEDs.
        """
        self.sense_hat.set_pixels(self.pixels)
