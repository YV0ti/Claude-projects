class Pet:

    total = 0

    def __init__ (self, name, breed, age, species, adopted = False):
        print('This is your brand new pet! YAYAYAAAA')
        Pet.accepted_species(species)
        self.name = name
        self.breed = breed
        self.__age =  age
        self.adopted = adopted
        self.species = species
        if self.__age < 0:
            raise ValueError("the dog has to be alive bub!")
        Pet.total += 1

    def adopt(self):
        if self.adopted == True:
            print("I'M SO SORRY :( the pet is already adopted (yes yes very sad or something, sooooo you wanna buy another one?)") 
        else:
            if self.adopted == False:
                print("YAYYYYYYYYY the pet is available for adoption!")
 
    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if new_age >= 0:
            self.__age = new_age
        else:
            print("enter an actual age bub it won't work otherwise")

    @staticmethod
    def accepted_species(species):
        allowed_species = ["cat", 'dog', 'rabbit', 'bird']
        if species in allowed_species:
            print("yeah okay you can come in")
        else:
            print("your name ain't on the list pal, now beat it before I break your knee caps capiche?")
            
    def describe(self):
        return (f'{self.name} is a {self.species} its {self.__age} years old and also a {self.breed} and the pet is {self.adopted}')

rex = Pet("Rex", "Lab", 5, 'dog')
print(rex.describe())
rex.adopt()


p = Pet("superdog", "golden", 2, 'dog')
print(p.describe())
p.adopt()


m = Pet("cuppy", "bark", 1200, 'shark')
print(m.describe())
m.adopt()


ghost = Pet("Ghost", "orange", 5, 'cat')
print(ghost.describe())
ghost.adopt()


print("you have", Pet.total, "pets")

rex.set_age(6)
print(f'the dog', rex.name, 'has a new age!', rex.get_age()) 