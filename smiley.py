from sense_hat import SenseHat


class Smiley:
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    BLANK = (0, 0, 0)

    def __init__(self, color="YELLOW"):
        # We have encapsulated the SenseHat object
        self.sense_hat = SenseHat()

        # self.color = color

        self.my_complexion = self.complexion(color)

        # Y = self.YELLOW
        Y = self.my_complexion
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

    def dim_display(self, dimmed=True):
        """
        Set the SenseHat's light intensity to low (True) or high (False)
        :param dimmed: Dim the display if True, otherwise don't dim
        """
        self.sense_hat.low_light = dimmed

    def show(self):
        """
        Show the smiley on the screen.
        """
        self.sense_hat.set_pixels(self.pixels)

    def complexion(self, colour):
        # TODO: Implement complexion() method (Done)
        match colour:
            case "WHITE":
                return self.WHITE
            case "GREEN":
                return self.GREEN
            case "RED":
                return self.RED
            case "YELLOW":
                return self.YELLOW
            case _:
                raise ValueError("Invalid Color")