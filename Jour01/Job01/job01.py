class Operation:
    # Constructeur de la classe Operation 
    def __init__(self, nombre1=0, nombre2=0):
        # Initialisation des attributs d'instance nombre1 et nombre2 avec les valeurs passées en arguments
        self.nombre1 = nombre1
        self.nombre2 = nombre2

# Instanciation d'un objet de la classe Operation sans passer d'arguments au constructeur
operation = Operation()
# Affichage de la représentation en chaîne de caractères de l'objet operation
print(operation)