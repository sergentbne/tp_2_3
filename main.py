from categorie import categorie
from invention import Invention
from binarytree import Node

racine = None


def ajouter_categorie(element, root=racine):
    if not root:
        root = categorie(element)
    elif root.value > element:
        ajouter_categorie(element, root.left)
    elif root.value < element:
        ajouter_categorie(element, root.right)
    return root


def ajouter_invention(nom_cat, nom, inventeur, date):
    return ajouter_categorie(nom_cat).ajouter_invention(Invention(nom, inventeur, date))


a = ajouter_invention("Physique", "Pendule", "Galilée", 1581)
b = ajouter_invention("Physique", "stuff", "Galilasdée", 1231)

print(b)


def afficher_categories_et_inventions(racine):
    print(racine)
