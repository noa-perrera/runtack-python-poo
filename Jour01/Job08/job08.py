class Livre:
    def __init__(self, titre, auteur, nombre_de_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_de_pages = nombre_de_pages
        self.__disponible = True

    def get_titre(self):
        return self.__titre

    def set_titre(self, titre):
        self.__titre = titre

    def get_auteur(self):
        return self.__auteur

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def get_nombre_de_pages(self):
        return self.__nombre_de_pages

    def set_nombre_de_pages(self, nombre_de_pages):
        if isinstance(nombre_de_pages, int) and nombre_de_pages > 0:
            self.__nombre_de_pages = nombre_de_pages
        else:
            print("Erreur: Le nombre de pages doit être un entier positif.")

    def verification(self):
        return self.__disponible

    def emprunter(self):
        if self.verification():
            self.__disponible = False
            return True
        else:
            return False

    def rendre(self):
        if not self.verification():
            self.__disponible = True
            return True
        else:
            return False
mon_livre = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 96)
print(mon_livre.get_titre())
print(mon_livre.get_auteur())
print(mon_livre.get_nombre_de_pages())
print(mon_livre.verification()) # Affiche True
mon_livre.emprunter() # Emprunte le livre
print(mon_livre.verification()) # Affiche False
mon_livre.rendre() # Rend le livre
print(mon_livre.verification()) # Affiche True