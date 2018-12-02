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
        
        self._nom = nom
        self._prenom = prenom
        self.age = age
        self._lieu_residence = lieu_residence
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
    
    def combien(cls):
        """Methode de classe (Methode statique) qui compte le nombre de Personne creer
        """
        print("Jusqu'a present il y a {} Personnes creer.".format(cls.personne_creer))
    
    combien = classmethod(combien)


    def _get_lieu_residence(self):
        """Methode qui sera appelee quand on souhaitera acceder en lecture a l'attribut 'lieu_residence
        """
        return self._lieu_residence

    def _set_lieu_residence(self, lieu):
        """Methode qui sera appelee quand on souhaitera acceder en ecriture a l'attribut 'lieu_residence
        """
        print("Attention il semble que {} demenage de {} a {}.".format(self.nom, self.lieu_residence,lieu))
        self._lieu_residence = lieu 


    def _set_nom(self, nom):
        """Setter pour l'attribut nom
        """
        print("Vous avez changer de nom de {} a {}.".format(self._nom, nom))
        self._nom = nom
    def _get_nom(self):
        """Getter de l'attribut nom
        """
        return self._nom 

    def _get_prenom(self):
        """Getter de prenom
        """
        return self._prenom
    def _set_prenom(self, prenom):
        """Setter
        """
        print("Attention tu vas changer ton prenom de {} a {}.".format(self._prenom, prenom))

    lieu_residence = property(_get_lieu_residence, _set_lieu_residence)# Il faut pas oublier """
    nom = property(_get_nom, _set_nom)
    prenom = property(_get_prenom, _set_prenom)

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

wafi.se_parler("Salut")

Personne.combien()#Methode de classe qui compte le nombre de Personne creer
Dupont.lieu_residence = "caca"#setter
print(Dupont.lieu_residence)#getter
wafi.prenom = "wafistos"
Dupont.nom = "dupont"


