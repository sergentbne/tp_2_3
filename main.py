import categorie
import invention
from binarytree import Node

root = None

def ajoute_categorie(element):
    if not root:
        root = categorie(element)
    if root.value > element:
        ajoute_categorie(root.left,element)
    elif root.value < element:
        ajoute_categorie(root.right,element)
     
    

