from categorie import categorie
from invention import Invention
from binarytree import Node

racine = categorie("Racine")

def ajouter_categorie(element,node=racine):
    global racine
    #print(element,"tries",racine, "to", node,"\n")

    if node.value < element:
        if node.right: ajouter_categorie(element, node.right)
        else: node.right = categorie(element)
    elif node.value > element:
        if node.left: ajouter_categorie(element, node.left)
        else: node.left = categorie(element)
    return node


def ajouter_invention(nom_cat, nom, inventeur, date):
    ajouter_categorie(nom_cat)#.ajouter_invention(Invention(nom, inventeur, date))


ajouter_categorie("Physique")
ajouter_invention("Maths", "Pendule", "Galilée", 1581)
ajouter_invention("Physique", "stuff", "Galilasdée", 1231)


def afficher_categories_et_inventions(root):
    print(root)


afficher_categories_et_inventions(racine)
