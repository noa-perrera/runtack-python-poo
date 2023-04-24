class Operation:
    # Constructeur de la classe Operation 
    def __init__(self, nombre1=0, nombre2=0):
        # Initialisation des attributs d'instance nombre1 et nombre2 avec les valeurs passées en arguments
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    # Méthode d'instance addition qui calcule la somme des attributs d'instance nombre1 et nombre2
    def addition(self):
        # Calcul de la somme des attributs d'instance nombre1 et nombre2
        resultat = self.nombre1 + self.nombre2
        # Affichage du résultat en utilisant une chaîne de formatage
        print(f"Le résultat de l'addition est {resultat}")

# Instanciation d'un objet de la classe Operation en passant les arguments 12 et 3 au constructeur
operation = Operation(12, 3)
# Appel de la méthode d'instance addition sur l'objet operation pour calculer et afficher la somme de ses attributs d'instance nombre1 et nombre2
operation.addition()