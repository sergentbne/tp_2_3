from invention import Invention
from binarytree import Node


class categorie(Node):
    def __init__(self, nom):
        super.__init__()
        self.__nom = nom
        self.__invention = []

    def ajouter_invention(self, invention):
        if type(invention) is Invention:
            raise TypeError("objet n'est pas de type invention")
        self.__invention.append(invention)

    def get_nom(self):
        return self.__nom

    def __str__(self):
        print(", ".join(self.__invention))
