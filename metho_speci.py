"""Suite du cours de OPENCLASSROOM sur les methodes speciales 
"""
"""Les methodes spaciales :
    def __ini__(self) : Constructeur
    def __del__(self) : Destructeur
    def __repr__(self): affiche l'objet 
    def __str__ (self): affiche l'objet egalement
    def __getattr__(self): Methode permet de definir une methode d'accees a nos attributs
    def __setattr__(self, mon_attr, val_attr)
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
        return "Personne:nom({}), prenom({}), age({})".format(self.nom, self.prenom, self.age)
    
    def __str__(self):
        """Affichage de l'objet
        """
        return "Personne:nom({}), prenom({}), age({})".format(self.nom, self.prenom, self.age)
    
    def __getattr__(self, adresse):
        """Affichage d'une alerte si l'attribut passe en argument n'est pas trouver 
        """
        print ("Alerte !!Il n'y a pas d'attribut {} ici.".format(adresse))
  
    def __delattr__(self, nom_attr):
        """On ne peut supprimer d'attribut, on leve une exception AttributeError
        """
        raise AttributeError("Vous ne pouvez pas supprimer aucun attribut de cette classe.")
#Programme pricipal 

h1 = Humain("MAMERI", "Wafi", 43)
print(h1)
h1.address 

