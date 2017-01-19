class People:
    def __init__(self, availability, name=""):
        self.availability = availability
        self.name = name

    def is_available(self, moment):
        return self.availability[moment]

