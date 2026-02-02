class Animal:
    def __init__(self , nom: str, nomscientif: str, taille: int):
        self.nom = nom
        self.nomscientif = nomscientif
        self.taille = taille

        def __str__(self) -> str:
            return '...' + self.getnom() + '...'

