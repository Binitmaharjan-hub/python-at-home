class animal:
    print("this is a class of animal")

class pet(animal):
    print("this is a class of pet")

class dog(pet):
    def bark(self):
        print("dog is barking")

a=dog()
a.bark()