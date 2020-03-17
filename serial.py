"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """Create serial generator with starting value of input"""
        self.start = start
        self.number = start
        self.begun = False

    def generate(self):
        """Increases the number value by one and returns it"""
        if not self.begun:
            self.begun = True
            return self.number
        else:
            self.number += 1
            return self.number

    def reset(self):
        """Sets the number value back to the original start value"""
        self.number = self.start
        self.begun = False