class Invention:
    def __init__(self, nom, inventeur, annee):
        self.__nom = nom
        self.__inventeur = inventeur
        self.__annee_creation = annee

    def __str__(self):
        return f"{self.__nom}, de {self.__inventeur}, en {self.__annee_creation}"
        

    def get_nom(self) -> str:
        return self.__nom

    def set_nom(self, nom) -> None:
        self.__nom = nom

    def get_inventeur(self) -> str:
        self.__inventeur

    def set_inventeur(self, inv) -> None:
        self.__inventeur = inv

    def get_annee(self):
        return self.__annee_creation

    def set_annee(self, annee):
        self.__annee_creation = annee
