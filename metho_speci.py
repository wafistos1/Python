"""Suite du cours de OPENCLASSROOM sur les methodes speciales 
"""
"""Les methodes spaciales :
    def __ini__(self) : Constructeur
    def __del__(self) : Destructeur
    def __repr__(self): affiche l'objet 
    def __str__ (self): affiche l'objet egalement
    def __getattr__(self): Methode permet de definir une methode d'accees a nos attributs
    def __setattr__(self, mon_attr, val_attr)
    Les methodes conteneur:(surcharge des operateurs)


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
"""--------------------------------------------------------------------------------------------------------"""

class ZDict:
    """Classe enveloppe d'un dictionnaire 
    """
    def __init__(self):
        """ Constructeur de la classe sans aucun parametres
        """
        self._dictionnaire = {}
    
    def __getitem__(self, index):
        """ Cette methode speciale est appelee quand on fait objet[index]
        Elle redirige vers self._dictionnaire[index]
        """
        print("valeur de retour est :")
        return self._dictionnaire[index]
    
    def __setitem__(self, index, valeur):
        """ Cette methode speciale est appelee quand on ecrit objet[index] = valeur
        On redirige vers self._dictionnaire[index] = valeur
        """
        
        self._dictionnaire[index] = valeur
        print("Dans l'index {} on vas ajoute le valeur {}.".format(index, valeur))
   
    def __delitem__(self, index):
        """Cette methode speciale est appelee quand on veut supprime une valeur 
        """
        del self._dictionnaire 
    def __repr__(self):
        """Cette methode speciale est pour afficher l'objet
        """
        return ("Vous avez dans ton dictionnaire plusieur valeurs")
    def __str__(self):
        """Cette methode est pour le print 
        """
        return ("Vous etes dans le dictionnaire {}".format(self._dictionnaire))
    
"""---------------------------------------------------------------------------------------"""
class Duree:
    """Classe contenant des durees sous la forme d'un nombre de minutes et de secondes
    """
    def __init__(self, min=0, sec=0):
        """Constructeur de la classe 
        """
        self.min = min  
        self.sec = sec
    def __str__(self):
        """Affichage de l'objet
        """
        return ("{0:02}:{1:02}".format(self.min, self.sec))
    def __add__(self, secondes):
        """Redefinition de l'operateur + sur l'objet Duree
        """
        nouvelle_dure = Duree()
        nouvelle_dure.min = self.min
        nouvelle_dure.sec = self.sec

        nouvelle_dure.sec += secondes

        if nouvelle_dure.sec >= 60:
            nouvelle_dure.sec %= 60
            nouvelle_dure.min +=1
        return nouvelle_dure
    def __sub__(self, secondes):
        """Surcharge de l'operateur - sur l'objet Duree
        """
        
    





#Programme pricipal 
temp = Duree(3, 5)
temp += 58 

print(temp)


