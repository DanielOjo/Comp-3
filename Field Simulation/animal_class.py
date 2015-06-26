#Daniel Ogunlana
#12/06/2015
#Task Animal

import random

class Animal:
    """A geneic food crop"""
    #constructor
    def __init__(self,growth_rate, light_need,water_need, name):
        #set the attributes with am inital value
        self._weight = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._food_need = light_need
        self._water_need = water_need
        self._status = "Baby"
        self._type = "Generic"
        self._growth = 0
        self._name = name
        #the above attributes are prefixed with an underscore to indicate
        #that they should not be accessed directly from outwith the class

    def needs(self):
        #return a dictionary containing the light and water needs
        return{"food need":self._food_need,"water need":self._water_need}

    #method to report the provide information about the current state
    #of the animal
    def report(self):
        return{"type":self._type, "status":self._status, "growth":self._growth, "days growing":self._days_growing, "name":self._name}

    def _update_status(self):
        if self._growth > 15:
            self._status = "Old"
        elif self._growth > 10:
            self._status = "Mature"
        elif self._growth > 5:
            self._status = "Young"
        elif self._growth > 0:
            self._status = "Child"
        elif self._growth == 0:
            self._status = "Baby"

    def grow(self,food,water):
        if food >= self._food_need and water >= self._water_need:
            self._growth += self._growth_rate
        #increment days growing
        self._days_growing += 1
        #update the status
        self._update_status()

def auto_age(animal,days):
    #age the animal
    for day in range(days):
        food = random.randint(1,10)
        water = random.randint(1,10)
        animal.grow(food,water)

def manual_age(animal):
    #get the light and water values from the user
    valid = False
    while not valid:
        try:
            food = int(input("Please enter a food value between 1-10: "))
            if 1 <= food <= 10:
                valid = True
            else:
                print("Please enter a valid number between 1-10")
        except ValueError:
            print("Please enter a valid number between 1-10")
    valid = False
    while not valid:
        try:
            water = int(input("Please enter a water value between 1-10: "))
            if 1 <= water <= 10:
                valid = True
            else:
                print("Please enter a valid water value between 1-10")
        except ValueError:
            print("Please enter a valid water value between 1-10")
    #gorw the crop
    animal.grow(food,water)
    print()
        
def display_menu():
    print("1. Age manually over 1 day")
    print("2. Age automatically over 30 days")
    print("3. Report status")
    print("0. Exit program")
    print()
    print("Please select an option from the above menu")

def get_menu_choice():
    option_valid = False
    while not option_valid:
       try:
           choice = int(input("Option Selected: "))
           if 0 <= choice <= 4:
               option_valid = True
           else:
               print("Please enter a valid option")
       except ValueError:
            print("Please enter a valid option")
    print()
    return choice

def manage_animal(animal):
    print("This is the animal management program")
    print()
    noexit = True
    while noexit:
        display_menu()
        option = get_menu_choice()
        print()
        if option == 1:
            manual_age(animal)
        elif option == 2:
            auto_age(animal,30)
        elif option == 3:
            print(animal.report())
            print()
        elif option == 0:
            noexit = False
            print()
    print("Thank you for using the aniaml management program")
                                    
def main():
    #instanciate the class
    new_animal = Animal(1,4,3, "John")
    manage_animal(new_animal)

    

if __name__ == "__main__":
    main()

