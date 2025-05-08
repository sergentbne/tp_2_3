from categorie import categorie
from invention import Invention
from binarytree import Node

racine = categorie("Racine")
liste_categories = [racine]


class arbre_binaire:
    def __init__(self):
        self.__racine = categorie("Racine")

    def ajouter_ou_trouver_categorie(self, element: str, node=None) -> categorie:
        if node is None:
            node = self.__racine
        # print(element,"tries",racine, "to", node,"\n")

        if node.value < element:
            if node.right:
                self.ajouter_ou_trouver_categorie(element, node.right)

            else:
                node.right = categorie(element)

        elif node.value > element:
            if node.left:
                self.ajouter_ou_trouver_categorie(element, node.left)

            else:
                node.left = categorie(element)

        return node

    def ajouter_invention(
        self, nom_cat: str, nom: str, inventeur: str, date: int
    ) -> None:
        classe_de_categorie = self.ajouter_ou_trouver_categorie(nom_cat)
        print(classe_de_categorie.value)
        classe_de_categorie.ajouter_invention(Invention(nom, inventeur, date))

    def crawler(self, nb_iter: int = 0, root=None) -> set:
        crawler = list()
        if nb_iter == 0:
            root = self.__racine
            print(self.__racine)

        if root.left:
            [crawler.append(i) for i in self.crawler(nb_iter + 1, root=root.left)]
        if root.right:
            [crawler.append(i) for i in self.crawler(nb_iter + 1, root=root.right)]
        crawler.append(root.value)

        return crawler


arbre = arbre_binaire()
arbre.ajouter_ou_trouver_categorie("Physique")
arbre.ajouter_invention("Maths", "Pendule", "Galilée", 1581)
arbre.ajouter_invention("Physique", "stuff", "Galilasdée", 1231)
print(arbre.crawler())
print(racine)


def afficher_categories_et_inventions(root):
    print(root)
    for i in liste_categories:
        print(arbre.crawler())


# afficher_categories_et_inventions(racine)
