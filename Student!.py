class Student:
    def __init__(self, name, year, major):
        self.name = name
        self.major = major
        self.year = year

    def str(self):
        return f'name: {self.name}, age: {self.year}, major: {self.major}'
    

Steve = Student('Steve Schulz', 23, 'English')
Johny = Student('Jonathan Rosenberg', 24, 'Biology')
Penny = Student('Penelope Meramveliotakis', 21, 'Physics')

print(Steve)
print(Johny)
print(Penny)
