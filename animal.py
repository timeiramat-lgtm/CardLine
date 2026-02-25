class Animal:
    def __init__(self , nom: str, nomscientif: str, taille: int):
        self.nom = nom
        self.nomscientif = nomscientif
        self.taille = taille

    def get_nom(self):
        return self.nom
    
    def get_nomscientif(self):
        return self.nomscientif

    def __str__(self):
        return f"{self.nom} ({self.nomscientif})"


    def comparer(self, other: Animal) -> bool:
    """ Permet de comparer l'instance courante de classe avec un de ses semblables
        :param other: l'autre animal objet de la comparaison
        :return: True si l'instance courante est plus petite de par la taille que l'instance other. False sinon
        """
        return self.taille < other.taille


    

    

        

