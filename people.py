class People:
    def __init__(self, availability, name="", motivation_score=1):
        self.availability = availability
        self.name = name
        self.motivation_score = motivation_score

    def is_available(self, moment):
        return self.availability[moment]

