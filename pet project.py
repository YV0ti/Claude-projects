class Pet:

    total = 0

    def __init__ (self, name, breed):
        print('This is your brand new pet! YAYAYAAAA')
        self.name = name
        self.breed = breed
        self.age =  0
        Pet.total += 1

      