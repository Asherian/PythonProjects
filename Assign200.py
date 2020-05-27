"""ABSTRACTION ASSIGNMENT
Create a class that utilizes the concept of abstraction.

1. Your class should contain at least one abstract method and one regular method.

2. Create a child class that defines the implementation of its parents abstract method.

3. Create an object that utilizes both the parent and child methods.
"""

from abc import ABC, abstractmethod

class ghoti(ABC):
    def scales(self, fish):
        print("Swimming along in the ocean along goes a",fish)
    #Calling abstract method so pass function will pass
    @abstractmethod 
    def fishing(self, fish):
        pass
class shark(ghoti):
    def fishing(self, fish):
        print('The {} looks at you and starts swimming closer, move fast!'.format(fish))

object = shark()
object.scales("shark")
object.fishing("shark")
