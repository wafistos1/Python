"""La suite du cours de OPENCLASSROOM l'HERITAGE 

    Les Fonctions bien pratiques
        issubclass : verifie si une classe est une sous-classe  d'une autre classe 
        isinstance : si un objet st issu d'une clase ou de ses classes filles

"""



class Personne:
    def __init__(self, nom):
        """Constructeur de notre classe 
        """
        self.nom = nom
        self.prenom = "Martin"
    
    def __str__(self):
        return "{0} {1}".format(self.prenom, self.nom)

class AgentSpecial(Personne):
    """Une classe qui herite de personne 
    """
    def __init__(self, nom, matricule):
        """Un agent se dfinit par son nom et son matricule
        """
        Personne.__init__(self, nom)
        """Faire appelee le Constructeur de la classe mere pour initialiser les attributs herite de la classe mere  
        """
        self.matricule = matricule 
    def __str__(self):
        """Methode appelee lors d'une conversion de l'objet en chaine 
        """
        return "Agent {0}, matricule {1}".format(self.nom, self.matricule)


#Programme pricipal

agent = AgentSpecial("Wafi", "34321")



print(issubclass(AgentSpecial, Personne))