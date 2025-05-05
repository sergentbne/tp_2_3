from categorie import categorie
from invention import Invention
from binarytree import Node

racine = categorie("0")

def ajouter_categorie(element, root = racine):
    print(root)
    if root == categorie("0"):
        root = categorie(element)
    elif root.value> element:
        ajouter_categorie(element, root.left)
    elif root.value < element:
        ajouter_categorie(element, root.right)
    return root


def ajouter_invention(nom_cat, nom, inventeur, date):
    ajouter_categorie(nom_cat).ajouter_invention(Invention(nom, inventeur, date))

ajouter_categorie("Physique")

ajouter_invention("Physique", "Pendule", "Galilée", 1581)
ajouter_invention("Physique", "stuff", "Galilasdée", 1231)


# def afficher_categories_et_inventions(root):
#     print(root)

afficher_categories_et_inventions(racine)
