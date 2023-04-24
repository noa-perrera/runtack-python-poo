class Student:
    def __init__(self, nom, prenom, numero_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__credits = 0
        self.__level = self.__studentEval()

    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
            self.__level = self.__studentEval()

    def get_credits(self):
        return self.__credits

    def __studentEval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def studentInfo(self):
        print(f"Nom: {self.__nom}\nPrenom: {self.__prenom}\nNumero d'etudiant: {self.__numero_etudiant}\nNiveau: {self.__level}")

john = Student("John", "Doe", 145)
john.add_credits(25)
john.add_credits(25)
john.add_credits(25)
print(f"Le nombre de crédits de {john._Student__nom} {john._Student__prenom} est de {john.get_credits()} points.")
john.studentInfo()