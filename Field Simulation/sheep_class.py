#Daniel Ogunlana
#23/06/2014
#Task Animal Cow

from animal_class import *

class Sheep(Animal):
    """A Sheep"""

    #constructor
    def __init__(self):
        #call the parent class constructor with default values for potato
        #growth rate =1; light need = 3; water need = 6
        super().__init__(1,3,6)
        self._type = "Sheep"
        self._name = "Charlie"

    #override grow method for subclass
    def grow(self,food,water):
        if food >= self._food_need:
            if self._status == "Mature":
                self._growth += self._growth_rate * 0.5
            elif self._status == "Baby":
                self._growth += self._growth_rate + 2.50
            else:
                self._growth += self._growth_rate
            #Increment day growing
            self._days_growing += 1
            #update the status
            self._update_status()

def main():
    #create a new cow
    sheep_animal = Sheep()
    print(sheep_animal.report())
    #manually age the cow
    manual_age(sheep_animal)
    print(sheep_animal.report())
    manual_age(sheep_animal)
    print(sheep_animal.report())

if __name__ == "__main__":
    main()
