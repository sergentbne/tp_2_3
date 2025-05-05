from invention import Invention
from binarytree import Node


class categorie(Node):
    def __init__(self, nom):
        super().__init__(nom)
        self.__inventions_dict = dict()

    def ajouter_invention(self, invention: Invention):
        if type(invention) is not Invention:
            raise TypeError("objet n'est pas de type invention")
        self.__inventions_dict[invention.get_nom()] = invention

    def get_nom(self):
        return self.__nom

    def __str__(self):
        return ", ".join(self.__inventions_dict)

    def get_value(self):
        return self.value
