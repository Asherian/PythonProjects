"""
ENCAPSULATION ASSIGNMENT
Create a class that uses encapsulation.

1. This class should make use of a private attribute or function.

2. This class should make use of a protected attribute or function.

3. Create an object that makes use of protected and private.
"""

class Encapsulated:
    def __init__(self):
        self._protVar = "Protected is one underscore."
        self.__priVar = "Double underscore denotes private variables."


    def RunPandP(self):
        print(self._protVar, self.__priVar)


        
if __name__ == "__main__":
    job = Encapsulated()
    job.RunPandP()


