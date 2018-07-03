from animal import Animal


class Horse (Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        self.sound = "neigh"
