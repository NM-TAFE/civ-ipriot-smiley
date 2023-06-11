from sense_hat import SenseHat


class Smiley:
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    BLANK = (0, 0, 0)

    def __init__(self, describe=False):
        # We have encapsulated the SenseHat object
        self.sense_hat = SenseHat()
        self.describe = describe

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

    def describe_state(self):
        """Generate a basic textual description of the current state."""
        return "Generic smiley face"
    
    
    def dim_display(self, dimmed=True):
        """
        Set the SenseHat's light intensity to low (True) or high (False)
        :param dimmed: Dim the display if True, otherwise don't dim
        """
        self.sense_hat.low_light = dimmed
        if self.describe:
            print("Display dimmed" if dimmed else "Display brightened")
            

    def show(self):
        """
        Show the smiley on the screen.
        """
        self.sense_hat.set_pixels(self.pixels)
        if self.describe:
            print(self.describe_state())
