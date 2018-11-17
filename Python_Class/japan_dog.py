# define the class of japan dog as a module


class JapanDog:
    def __init__(self, name ,age):
        self.name = name
        self.age = age

    def get_dog_age(self):
        print(self.age)

    def get_dog_name(self):
        print(self.name)
