import categorie
import invention
from binarytree import Node

racine = None

def ajouter_categorie(element, root = racine):
    if not root:
        root = categorie(element)
    elif root.value > element:
        ajouter_categorie(element,root.left)
    elif root.value < element:
        ajouter_categorie(element,root.right)
    return root


def ajouter_invention(nom_cat,nom,inventeur,date):
    ajouter_categorie(nom_cat).ajouter_invention(invention(nom,inventeur,date))
    
ajouter_invention("Physique", "Pendule", "Galilée", 1581)
     
def afficher_categories_et_inventions(racine):
    print(racine)
