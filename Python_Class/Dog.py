# 本プロジェクトの紹介類の基本的な知識


class Dog:
    """Just mimick the behavior of a small dog"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        """mimick the action of a small dog """
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """mimick the rollover of a small dog"""
        print(self.name.title() + " rolled over before you!")


# 実例化
my_dog = Dog('kawayi kitty', 10)
my_dog.sit()
my_dog.roll_over()


