import time
from blinkable import Blinkable
from smiley import Smiley, SenseHat

class Angry(Smiley, Blinkable):

    def __init__(self, color="RED"):
        super().__init__(color=color)

        self.draw_mouth()
        self.draw_eyes()
        self.draw_eyebrows()

    def draw_mouth(self):
        """
        Method that draws the mouth on the standard faceless smiley.
        """
        # mouth = [41, 46, 50, 51, 52, 53]
        mouth = list(range(41, 46+1))
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        """
        Method that draws the eyes (open or closed) on the standard smiley.
        :param wide_open: True if eyes opened, False otherwise
        """
        # eyes = [26, 29, 18, 21]
        eyes = [26, 29]
        for pixel in eyes:
            # self.pixels[pixel] = self.BLANK if wide_open else self.my_complexion
            self.pixels[pixel] = self.YELLOW if wide_open else self.my_complexion

    def draw_eyebrows(self):
        # TODO: Implement Eyebrows for Angry

        # eyebrows = [1, 10, 19, 6, 13, 20]
        eyebrows = [10, 19, 13, 20]
        for pixel in eyebrows:
            self.pixels[pixel] = self.BLANK

    def blink(self, delay=0.25):
        """
        Make the happy smiley blink once with a certain delay (in s).
        This is the implementation of the abstract method from the
        Blinkable abstract class.

        :param delay: Delay in seconds
        """
        self.draw_eyes(wide_open=False)
        self.show()
        time.sleep(delay)
        self.draw_eyes(wide_open=True)
        self.show()
