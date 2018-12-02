#Tuto de OPENCALSSROOM sur le langage python 

class Personne:
    """ Classe definissant une personne caracterisee par:
    -son nom
    -son premon
    -son age
    -son lieu de residence"""

    personne_creer = 0#compteur de personne creer

    def __init__(self, nom="Dupont", prenom="Jean", age=33, lieu_residence="Paris"):
        """Constructeur de notre calsse. Chaque attribut va etre instancie
            avec une valeur par defaut ...
        """
        
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.lieu_residence = lieu_residence
        Personne.personne_creer +=1#C'est un attribu statique 
    
    def se_presente(self):
        """ Methode qui presente la Personne 
        """
        print("Je suis {} {} j'ai {} et j'habite {}".format(self.nom, self.prenom, self.age, self.lieu_residence))
     
    def se_parler(self, message):
        """Methode qui fait la discution entre les personnages 
        """
        message = message.capitalize()
        if message in "Bonjour":
            print("Bonjour toi !!! comment cava??")
        elif message in "Salut":
            print("C'est pas le moment de dire salut!! il faut dire Bonjour !!")
        else:
            print("J'ai pas compris votre question il faut commencer pas dire Bonjour")

    
   

""" Programme principal"""

wafi = Personne()
wafi.nom = "MAMERI"
wafi.prenom = "Wafi"
wafi.age = 43
wafi.lieu_residence = "Alger"
wafi.se_presente()

Dupont = Personne()
Dupont.se_presente()

print(Personne.personne_creer)

wafi.se_parler("bonjour")

