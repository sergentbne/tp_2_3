from invention import Invention


class categorie:
    def __init__(self, nom):
        self.__nom = nom
        self.__invention = []

    def ajouter_invention(self, invention):
        if type(invention) is Invention:
            raise TypeError("objet n'est pas de type invention")
        self.__invention.append(invention)

    def __str__(self):
        print(", ".join(self.__invention))
