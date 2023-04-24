class Voiture:
    def __init__(self, marque, modele, annee, kilometrage, en_marche=False, reservoir=50):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = en_marche
        self.__reservoir = reservoir

    # Mutateurs et accesseurs pour chaque attribut
    def get_marque(self):
        return self.__marque

    def set_marque(self, marque):
        self.__marque = marque

    def get_modele(self):
        return self.__modele

    def set_modele(self, modele):
        self.__modele = modele

    def get_annee(self):
        return self.__annee

    def set_annee(self, annee):
        self.__annee = annee

    def get_kilometrage(self):
        return self.__kilometrage

    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage

    def get_en_marche(self):
        return self.__en_marche

    def set_en_marche(self, en_marche):
        self.__en_marche = en_marche

    # Méthodes demarrer et arreter
    def demarrer(self):
        if self.verifier_plein() > 5:
            self.__en_marche = True

    def arreter(self):
        self.__en_marche = False

    # Méthode privée verifier_plein
    def verifier_plein(self):
        return self.__reservoir
ma_voiture = Voiture(marque="Toyota", modele="Corolla", annee=2020, kilometrage=10000)

# Afficher les attributs de la voiture
print(ma_voiture.get_marque())
print(ma_voiture.get_modele())
print(ma_voiture.get_annee())
print(ma_voiture.get_kilometrage())

# Démarrer la voiture
ma_voiture.demarrer()
print(ma_voiture.get_en_marche())

# Arrêter la voiture
ma_voiture.arreter()
print(ma_voiture.get_en_marche())