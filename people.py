class People:
    def __init__(self, dispos):
        self.dispos = dispos

    def is_available(self, moment):
        return self.dispos[moment]

