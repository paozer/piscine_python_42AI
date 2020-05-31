from time import time, sleep
from random import randint


class CoffeeMachine():

    water_level = 100

    def log(fct):
        def wrapper(*args, **kwargs):
            start = time()
            ret = fct(*args, **kwargs)
            end = time()
            s = ""
            if str(fct.__name__) is "start_machine":
                s += "Start Machine"
            elif str(fct.__name__) is "boil_water":
                s += "Boil Water"
            elif str(fct.__name__) is "make_coffee":
                s += "Make Coffee"
            elif str(fct.__name__) is "add_water":
                s += "Add Water"
            s += (f"\tduration: {end - start:8.6f}s\n")
            with open("machine.log", "a") as f:
                f.write(s)
            return ret
        return wrapper

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        print("Please add water!")
        return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":

    f = open("machine.log", "w")
    f.close()

    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
