from animal import Animal
from horse import Horse
from pig import Pig

if __name__ == "__main__":
    cow = Animal()
    cow.speak()
    horse = Horse("Bill")
    horse.speak()
    horse2=Horse ("Joe")
    horse.get_name()
    horse2.get_name()
    pig=Pig ("Rob")
    pig.speak ()
    pig.get_name()