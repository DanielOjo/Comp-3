#Daniel Ogunlana
#23/06/2015
#Task 9 - 12 Field Class
#task 13 (06:23)

from potato_class import *
from wheat_class import *
from sheep_class import *
from cow_class import *

class Field:
    """Simulate a field that can contain animeal and crops"""

    #constructor
    def __init__(self,max_animals,max_crops):
        self._crops = []
        self._animals = []
        self._max_animals = max_animals
        self._max_crops = max_crops

    def plant_crop(self,crop):
        if len(self._crops) < self._max_crops:
            self._crops.append(crop)
            return True

    def add_animal(self, animal):
        if len(self._animals) < self._max_animals:
            self._animals.append(animal)
            return True
        else:
            return False

    def harvest_crop(self,position):
        return self._crops.pop(position)

    def remove_animal(self,position):
        return self._animals.pop(position)
    
    def report_contents(self):
        crop_report = []
        animal_report = []
        for crop in self._crops:
            crop_report.append(crop.report())
        for animal in self._animals:
            animal_report.append(animal.report())
        return {"crops": crop_report, "animals" : animal_report}

    def report_needs(self):
        food = 0
        light = 0
        water = 0
        for crop in self._crops:
            needs = crop.needs()
            if needs["light need"] > light:
                light = needs["light need"]
            if needs["water need"] > water:
                water = needs["water need"]
        for animal in self._animals:
            needs = animal.needs()
            food += needs["food need"]
            if needs["water need"] > water:
                water -= needs["water need"]
        return {"food":food,"light":light,"water":water}

    def grow(self,light,food,water):
        #grow the crops (light and water are available to all crops in the same amo
        if len(self._crops) >0:
            for crop in self>_crops:
                crop.grow(light,water)
        if len(self._animals) > 0:
            #grow the animals (water available to all animals in the same amounts
            #but food is a total that must be shared
            food_required = 0
            #get a total of the food required by the animals on the field
            for animal in self._animals:
                needs = animals.needs()
                food_required += need["food need"]
            #if we have more food available than is required work out the additional
            #availble food
            if food > food_required:
                additonal_food = food - food_required
                food = food_required
            else:
                additional_food = 0
            #grow each animal
            for animal in self._animals:
                #get the animals food needs
                needs = animal.needs()
                if food >= needs["food need"]
                food -= needs["food need"]
                

def display_crops(crop_list):
    print()
    print("The following crops are in thid field: ")
    pos = 1
    for crop in crop_list:
        print("{0:>2}. {1}".format(pos,crop.report()))
        pos += 1

def display_animals(animal_list):
    print()
    print("The following animals in this field are: ")
    pos = 1
    for animal in animal_list:
        print("{0:>2}. {1}".format(pos,animal.report()))
        pos += 1

def select_crop(length_list):
    valid = False
    while not valid:
        selected = int(input("Please select a crop: "))
        if selected in range(1,length_list+1):
            valid = True
        else:
            print("Please select a valid option")
    return selected -1

def select_animal(length_list):
    valid = False
    while not valid:
        selected = int(input("Please select an animal: "))
        if selected in range(1,length_list+1):
            valid = True
        else:
            print("Please select a valid option")
    return selected -1

def harvest_crop_from_field(field):
    display_crops(field._crops)
    selected_crop = select_crop(len(field._crops))
    return field.harvest_crop(selected_crop)

def remove_animal_from_field(field):
    display_animals(field._animals)
    selected_animal = select_animal(len(field._animals))
    return field.remove_animal(selected_animal)
    
def main():
    new_field = Field(5,2)
    new_field.plant_crop(Wheat())
    new_field.plant_crop(Potato())
    new_field.add_animal(Sheep("Luke"))
    new_field.add_animal(Cow("Chris"))
    report = new_field.report_contents()
    print(report["animals"])
    print()
    print(report["crops"])
    report = new_field.report_needs()
    print(report)

if __name__ == "__main__":
          main()
