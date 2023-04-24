class Personne:
    # Constructeur de la classe Personne 
    def __init__(self, nom, prenom):
        # Initialisation des attributs d'instance nom et prenom avec les valeurs passées en arguments
        self.nom = nom
        self.prenom = prenom

    # Méthode d'instance se_presenter qui renvoie une chaîne de caractères présentant la personne
    def se_presenter(self):
        # Renvoi d'une chaîne de caractères présentant la personne en utilisant une chaîne de formatage
        return f"Je suis {self.prenom} {self.nom}"

# Instanciation de deux objets de la classe Personne en passant des arguments différents au constructeur
personne1 = Personne("Doe", "John")
personne2 = Personne("Smith", "Jane")

# Appel de la méthode d'instance se_presenter sur les objets personne1 et personne2 pour afficher leur présentation en console
print(personne1.se_presenter())
print(personne2.se_presenter())