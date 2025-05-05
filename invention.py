class Invention:
    def __init__(self, nom, inventeur, annee):
        self.__nom = nom
        self.__inventeur = inventeur
        self.__annee_creation = annee

    def __str__(self):
        print(
            f"nom de l'invention: {self.__nom}, nom de l'inventeur: {self.__} et année de création: {self.__annee_creation}"
        )
