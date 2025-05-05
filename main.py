import categorie
import invention
from binarytree import Node

root = Node("0")

def ajoute_categorie(root,element):
    if not root:
        root = categorie(element)
    if root.value > element:
        ajoute_categorie(root.left,element)
    elif root.value < element:
        ajoute_categorie(root.right,element)
     
    

