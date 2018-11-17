#  Here the file defines the class of UsDog
# Here it's about inheritance of class using super() method
from Dog import Dog


class UsDog(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_us_dog_name(self):
        print(self.name)

    def get_us_dog_age(self):
        dog_age = self.age
        return dog_age


# instantiation of this class
print("---us-dog---")
my_us_dog = UsDog('us-small-dog', 5)
my_us_dog.sit()
my_dog_age = my_us_dog.get_us_dog_age()
print("my us dog's age is " + str(my_dog_age))

