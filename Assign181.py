"""Create two classes that inherit from another class.

1. Each child should have at least two of their own attributes.

2. The parent class should have at least one method (function).

3. Both child classes should utilize polymorphism on the parent class method.

"""

#Parent class Alpha
class Magic:
    school = "Universal"
    speciality = False
    
    def spell(self):
        entry_school = input("Please respond Universal: ")
        entry_special = input("True or False, you want a speciality?: ")
        if (entry_school == self.school and entry_special == self.speciality):
            print("You want to try a bit of everything, that's great!")
        elif (entry_school == self.school and entry_special != self.speciality):
            print("You seem to be a little confused.")            
        elif (entry_school != self.school and entry_special == self.speciality):
            print("{} is the school of no speciality, you should try {} magics.".format(School))
        else:
            print("Maybe you'd rather try being a fighter?")


#Child class Bravo
class Abjuration(Magic):
    desc = "Protective Magics"
    school = "Abjuration"
    speciality = True
    restricts = "Necromancy and Evocation"
 
    def spell(self):
        entry_school = input("Please respond Abjuration: ")
        entry_special = input("True or False, you want a speciality?: ")
        if (entry_school == self.school and entry_special == self.speciality):
            print("You want to specialize in protective magics, wonderful!")
        elif (entry_school != self.school and entry_special == self.speciality):
            print("{} is the school of protective magic, but you'll lose out on {} magic.".format(self.school, self.restricts))
        else:
            print("Maybe you'd rather try being a fighter?")

#Child Class Catico
class Evocation(Magic):
    desc = "Damaging Magic"
    school = "Evocation"
    speciality = True
    restricts = "Abjuration and Conjuration"
 
    def spell(self):
        entry_school = input("Please respond Universal: ")
        entry_special = input("True or False, you want a speciality?: ")
        if (entry_school == self.school and entry_special == self.speciality):
            print("You want to go boom! Okay...")
        elif (entry_school != self.school and entry_special == selfspeciality):
            print("{} is a great school for explosions, but you'll loose out on {} magic.".format(self.school, self.restricts))
        else:
            print("Maybe you'd rather try being a fighter?")

magic = Magic()
magic.spell()

protect = Abjuration()
protect.spell()

boom = Evocation()
boom.spell()
    
