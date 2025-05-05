import categorie
import invention
from binarytree import Node

racine = Node(1)

def ajoute_elem(root,elem,type):
    if type(elem) != type:
        raise TypeError(str(elem)+" n'est pas de classe "+str(type))
    if not root.left:
        root.left = Node(elem)
    elif not racine.right:
        root.right = Node(elem)
    else:
        raise ValueError(str(root)+" noeud satiété")
