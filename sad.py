from smiley import Smiley


class Sad(Smiley):
    def __init__(self):
        super().__init__()

        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self):
        """
        Draws the mouth feature on a smiley
        """
        print(f"Drawing a {self.mood}, face: {self.emoji}")

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
        print(description)

        eyes = [10, 13, 18, 21]
        for pixel in eyes:
            if wide_open:
                eyes = self.BLANK
            else:
                eyes = self.YELLOW
            self.pixels[pixel] = eyes
