#Daniel Ogunlana
#11/06/2014
#Task Animal Cow

from animal_class import *

class Cow(Animal):
    """A Cow"""

    #constructor
    def __init__(self):
        #call the parent class constructor with default values for potato
        #growth rate =1; light need = 3; water need = 6
        super().__init__(1,3,6)
        self._type = "Cow"
        self._name = "John"

    #override grow method for subclass
    def grow(self,food,water):
        if food >= self._food_need:
            if self._status == "Young":
                self._growth += self._growth_rate * 1.5
            elif self._status == "Baby":
                self._growth += self._growth_rate + 1.25
            else:
                self._growth += self._growth_rate
            #Increment day growing
            self._days_growing += 1
            #update the status
            self._update_status()

def main():
    #create a new potato crop
    cow_animal = Cow()
    print(cow_animal.report())
    #manually grow the crop
    manual_age(cow_animal)
    print(cow_animal.report())
    manual_age(cow_animal)
    print(cow_animal.report())

if __name__ == "__main__":
    main()
