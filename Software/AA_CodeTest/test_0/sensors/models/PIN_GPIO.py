from gpiozero import LED
from time import sleep

class PIN_GPIO():
    output_15 = LED(15)

    def __init__(self, output_15):
        self.output_15 = output_15

    @property
    def get_output_15(self):
        return self.output_15
    @get_output_15.setter
    def set_output_15(self, value):
        self.output_15 = value