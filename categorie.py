from invention import Invention
from binarytree import Node


class Categorie(Node):
    def __init__(self, nom):
        super().__init__(nom)
        self.__inventions_dict = dict()

    def ajouter_invention(self, invention: Invention):
        if type(invention) is not Invention:
            raise TypeError("objet n'est pas de type invention")
        self.__inventions_dict[invention.get_nom()] = invention

    def afficher(self):
        if len(self.__inventions_dict) == 0:
            return ""
        return f"{self.value} , with: \n" + "\n".join(
            map(str, [self.__inventions_dict[x] for x in self.__inventions_dict])
        )

    def get_nom(self):
        return self.__nom

    def __str__(self):
        # return self.value + " , with ".join(self.__inventions_dict)
        return super().__str__()

    def get_inventions(self):
        return self.__inventions_dict
