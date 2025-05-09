from categorie import Categorie
from invention import Invention


class arbre_binaire:
    def __init__(self):
        self.__racine = Categorie("Racine")
        self.__racine_courante: Categorie

    def ajouter_ou_trouver_categorie(self, element: str, node=None) -> Categorie:
        if node is None:
            node = self.__racine
        # print(element,"tries",racine, "to", node,"\n")

        if node.value < element:
            if node.right:
                node = self.ajouter_ou_trouver_categorie(element, node.right)

            else:
                node.right = Categorie(element)
                return node.right

        elif node.value > element:
            if node.left:
                node = self.ajouter_ou_trouver_categorie(element, node.left)

            else:
                node.left = Categorie(element)
                return node.left

        return node

    def ajouter_invention(
        self, nom_cat: str, nom: str, inventeur: str, date: int
    ) -> None:
        classe_de_categorie = self.ajouter_ou_trouver_categorie(nom_cat)
        print("valeur de la racine:", classe_de_categorie.value)
        classe_de_categorie.ajouter_invention(Invention(nom, inventeur, date))

    def crawler(self, nb_iter: int = 0, root=None) -> list:
        crawler = list()
        if nb_iter == 0:
            root = self.__racine
        # Note -> faisait des listes inbriqué, donc dépacké avec ça
        if root.left:
            [crawler.append(i) for i in self.crawler(nb_iter + 1, root=root.left)]
        if root.right:
            [crawler.append(i) for i in self.crawler(nb_iter + 1, root=root.right)]
        crawler.append(root)

        return crawler

    def afficher_categories_et_inventions(self):
        print(self.__racine)
        for i in self.crawler():
            print(i.afficher())


arbre = arbre_binaire()
arbre.ajouter_ou_trouver_categorie("Physique")
arbre.ajouter_invention("Maths", "Pendule", "Galilée", 1581)
arbre.ajouter_invention("Physique", "stuff", "Galilasdée", 1231)
arbre.afficher_categories_et_inventions()
