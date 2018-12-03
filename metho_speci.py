"""Suite du cours de OPENCLASSROOM sur les methodes speciales 
"""
"""Les methodes spaciales :
    def __ini__(self) : Constructeur
    def __del__(self) : Destructeur
    def __repr__(self): affiche l'objet 


"""

class Humain:
    """ Une class simple pour mon exemple 
    """

    def __init__(self, nom, prenom, age):
        """Constructeur de la classe appelee quand l'objet est cree
        """
        self.nom = nom
        self.prenom = prenom
        self.age = age
        print("Un humain est cree .")
    def __del__(self):
        """Destructeur :Methode appelee quand l'objet est supprime
        """
        print("Un humain est supprime .")
    def __repr__(self):
        """affichage de l'objet 
        """
        print("Personne:nom({}), prenom({}), age({})".format(self.nom, self.prenom, self.age))


#Programme pricipal 

h1 = Humain("MAMERI", "Wafi", 43)
print(h1)