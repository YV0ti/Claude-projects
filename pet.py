class Pet:

    total = 0

    def __init__ (self, name, breed, age):
        print('This is your brand new pet! YAYAYAAAA')
        self.name = name
        self.breed = breed
        self.__age =  age
        Pet.total += 1

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if new_age >= 0:
            self.__age = new_age
        else:
            print("enter an actual age bub it won't work otherwise")

    def describe(self):
        return (f'{self.name} is a {self.__age} year old {self.breed}')

rex = Pet("Rex", "Lab", 5)
print(rex.describe())

p = Pet("superdog", "golden", 2)
print(p.describe())

m = Pet("dog", "bark", 1200)
print(m.describe())

print("you have", Pet.total, "dogs")

rex.set_age(6)
print(f'the dog', rex.name, 'has a new age!', rex.get_age) 