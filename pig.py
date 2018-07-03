from animal import Animal


class Pig (Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        self.sound = "oink"
    def speak(self):
        print ("Pigs always say", self.sound)