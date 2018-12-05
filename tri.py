from operator import itemgetter, attrgetter

class ligneInventaire:
    """Classe representant une ligne d'un inventaire de vente 
        Attribut attendus par le constructeur
            -produit -- le nom du produit
            -prix -- le prix du prodtuit
            -quantite -- la quantite vendu du produit

    
    
    """
    def __init__(self, produit, prix, quantite):
        self.produit = produit
        self.prix = prix
        self.quantite = quantite


    def __repr__(self):
        """Formatage de l'objet
        """
        return "Ligne d'inventaire {} ({} X {})\n".format(self.produit, self.prix, self.quantite)

#Programme pricipal

inventaire =[
    ligneInventaire("Pomme rouge", 1.2, 19),
    ligneInventaire("Orange", 1.4, 24),
    ligneInventaire("Banane", 0.9, 21),
    ligneInventaire("Poire", 1.2, 24)
]

print(sorted(inventaire, key=attrgetter("prix", "quantite")))