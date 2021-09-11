class Person:
    def __init__(self, name, age, team):
        self.name = name
        self.age = age
        self.team = team

    def birth_year(self):
        return 2021 - self.age

    def __str__(self):
        return "Name: {}, Age: {}, Team : {}".format(self.name, self.age, self.team)

armin = Person("Armin", 31, ["Arsenal", 'Perspolis'])
pouya = Person('Pouya', 30, ['Chelsea', 'Eseteghlal'])
people = (armin, pouya)
for person in people:
    print(person)