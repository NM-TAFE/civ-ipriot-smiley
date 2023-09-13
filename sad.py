from smiley import Smiley


class Sad(Smiley):
    """Challenges (repeated from smiley):
    1. Notice that all smileys inherit the mood of their parent!
    2. Make it so the mood is parameterised in both the parent and child
    3. ensure that the draw mouth correctly encapsulates the mood of the smiley
    """
    def __init__(self):
        super().__init__()

        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self):
        """
        Method that draws the mouth on the standard faceless smiley.
        """
        print(f"Drawing a {self.mood}, face: {self.emoji}")

        mouth = [49, 54, 42, 43, 44, 45]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        """
        Method that draws the eyes (open or closed) on the standard smiley.
        :param wide_open: True if eyes opened, False otherwise
        """
        description = f"{self.mood} eyes open" else "happy eyes closed"
        print(description)

        eyes = [10, 13, 18, 21]
        for pixel in eyes:
            self.pixels[pixel] = self.BLANK if wide_open else self.YELLOW
