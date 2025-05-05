# import categorie
# import invention
from binarytree import Node

racine = Node("Racine")

def ajoute_elem(root,elem):
    if not root.left:
        root.left = Node(elem)
    elif not racine.right:
        root.right = Node(elem)
    else:
        raise ValueError(str(root)+" noeud satiété")

ajoute_elem(racine,2,int)
ajoute_elem(racine,"3a",str)
print(racine)




