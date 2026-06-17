import random

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age



class Pirate(Human):
    def __init__(self, name, age, spawn, observation_haki=0, armament_haki=0, conquerors_haki=0):
        super().__init__(name, age)
        self.obs_haki = observation_haki
        self.armament_haki = armament_haki
        self.conqs_haki = conquerors_haki
        self.spawn = spawn

    def spawn_luck(self):
        observation_haki = random.randint(1, 100)
        armament_haki = random.randint(1, 100)
        conquerors_haki = random.randint(1, 100)
        seas = ["Paradise", "New World", "South Blue", "West Blue", "East Blue", "North Blue"]
        spawn = random.choice(seas)
        return observation_haki, armament_haki, conquerors_haki, spawn

    @classmethod
    def get(cls):
        name = input("Name: ")
        age = input("Age: ")
        return Pirate(name, age)

    def __str__(self):
        return f"{self.name}, is {self.age} years old and they were born and raised in the {self.spawn}.\n Their base observation level is {self.obs_haki} \n Their base armament level is {self.armament_haki} \n Their base conquerors level is {self.conqs_haki}"



def main():
    fun = Pirate.get()
    print(fun)


if __name__ == "__main__":
    main()
