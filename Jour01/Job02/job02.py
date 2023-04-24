class Operation:
    # Constructeur de la classe Operation 
    def __init__(self, nombre1=0, nombre2=0):
        # Initialisation des attributs d'instance nombre1 et nombre2 avec les valeurs passées en arguments
        self.nombre1 = nombre1
        self.nombre2 = nombre2

# Instanciation d'un objet de la classe Operation en passant les arguments 12 et 3 au constructeur
operation = Operation(12, 3)
# Affichage des attributs d'instance nombre1 et nombre2 de l'objet operation en utilisant une chaîne de formatage
print(f"le nombre1 est {operation.nombre1}\nle nombre2 est {operation.nombre2}")