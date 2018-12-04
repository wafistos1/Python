from operator import itemgetter, attrgetter


class Etudiants:
    """Classe representant un etudiant.
    
    On represente un etudiant par son :
    -prenom
    -age 
    -moyenne entre [0-20]
    
    """
    def __init__(self, nom, age, moyenne):
        """Constructeur de Classe
        """
        self.nom = nom
        self.age = age
        self.moyenne= moyenne
    def __repr__(self):
        """Affichage redifinition 
        """
        return "<Etudiant {} (age = {}, moyenne = {})>\n".format(self.nom, self.age, self.moyenne)

etudiants = [
    Etudiants("Clements", 14, 16),
    Etudiants("Charles", 12, 15),
    Etudiants("Oriane", 14, 18),
    Etudiants("Thomas", 11, 12),
    Etudiants("Damien", 12, 15)
]
print(sorted(etudiants, key=attrgetter("moyenne", "age")))

