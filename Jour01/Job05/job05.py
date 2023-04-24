class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.prenom = nom

animal = Animal()
print(f"L'âge de l'animal est {animal.age}")
animal.vieillir()
animal.nommer("Luna")
print(f"L'âge de l'animal est {animal.age}")
print(f"Le nom de l'animal est {animal.prenom}")