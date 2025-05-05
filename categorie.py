from invention import Invention
from binarytree import Node


class categorie(Node):
    def __init__(self, nom):
        super.__init__(nom)
        self.__inventions = dict()

    def ajouter_invention(self, invention: Invention):
        if type(invention) is Invention:
            raise TypeError("objet n'est pas de type invention")
        self.__invention[invention.get_nom] = invention.get_nom()

    def get_nom(self):
        return self.__nom

    def __str__(self):
        print(", ".join(self.__invention))
