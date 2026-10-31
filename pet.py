class Pet:

    total = 0

    def __init__ (self, name, breed, age, adopted = False):
        print('This is your brand new pet! YAYAYAAAA')
        self.name = name
        self.breed = breed
        self.__age =  age
        self.adopted = adopted
        if self.__age < 0:
            raise ValueError("the dog has to be alive bub!")
        Pet.total += 1

    def adopt(self):
        if self.adopted == True:
            print("I'M SO SORRY :( the dog is already adopted (yes yes very sad or something, sooooo you wanna buy another one?)") 
        else:
            if self.adopted == False:
                print("YAYYYYYYYYY the dog is available for adoption!")
 
    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if new_age >= 0:
            self.__age = new_age
        else:
            print("enter an actual age bub it won't work otherwise")

    def describe(self):
        return (f'{self.name} is a {self.__age} year old {self.breed} and the dog is {self.adopted}')

rex = Pet("Rex", "Lab", 5)
print(rex.describe())
rex.adopt()


p = Pet("superdog", "golden", 2)
print(p.describe())
p.adopt()


m = Pet("dog", "bark", 1200)
print(m.describe())
m.adopt()


ghost = Pet("Ghost", "cat", 5)
print(ghost.describe())
ghost.adopt()


print("you have", Pet.total, "dogs")

rex.set_age(6)
print(f'the dog', rex.name, 'has a new age!', rex.get_age()) 