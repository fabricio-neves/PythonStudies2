class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'Hi there! I am {self.name}!')


maria = Person('Maria')
maria.talk()
