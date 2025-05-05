import categorie
import invention
from binarytree import Node

root = None

def ajouter_categorie(element):
    if not root:
        root = categorie(element)
    if root.value > element:
        ajouter_categorie(root.left,element)
    elif root.value < element:
        ajouter_categorie(root.right,element)
    return root


def ajouter_invention(nom_cat,nomninventeur,date):
    ajouter_categorie(nom_cat).ajouter_invention
    

ajouter_invention("Physique", "Pendule", "Galilée", 1581)
     
    

