#Will McElwee
#12-17-24
#This program lets the user input data about their pet
#and it displays this information to them

def main():
    #Declare input variables
    input_name = ""
    input_type = ""
    input_age = 0

    #Create a pet object
    animal = Pet()

    #Get values for a pet
    input_name = input("Enter a pet name: ")
    input_type = input("Enter a pet type: ")
    input_age = input("Enter a pet age: ")

    #Constructor
    animal.construct(input_name, input_type, input_age)

    #Show values for this pet
    print(f"Your pet name: {animal.get_name()}")
    print(f"Your pet type: {animal.get_type()}")
    print(f"Your pet age: {animal.get_age()}")

class Pet:
    #Fields
    def _init_(self):
        self._name = ""
        self._type = ""
        self._age = 0

    #Constructor
    def construct(self, n, t, a):
        self._name = n
        self._type = t
        self._age = a

    #Mutators
    def set_name(self, n):
        self._name = n

    def set_type(self, t):
        self._type = t

    def set_age(self, t):
        self._age = a

    #Accessors
    def get_name(self):
        return self._name

    def get_type(self):
        return self._type

    def get_age(self):
        return self._age


main()
