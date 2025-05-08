from categorie import categorie
from invention import Invention
from binarytree import Node

racine = categorie("Racine")
liste_categories = [racine]



def ajouter_categorie(element,node=racine):
    global racine
    if node.value < element:
        if node.right: return ajouter_categorie(element, node.right)
        else: 
            node.right = categorie(element)
            liste_categories.append(node.right)
            return node.right
        
    elif node.value > element:
        if node.left: return ajouter_categorie(element, node.left)
        else: 
            node.left = categorie(element)
            liste_categories.append(node.left)
            return node.left
        
    return node




def ajouter_invention(nom_cat, nom, inventeur, date):
    ajouter_categorie(nom_cat).ajouter_invention(Invention(nom, inventeur, date))

def modifier_annee_invention(invention, date, node = racine):
    global racine
    if invention in node.get_inventions():
        print ("yes")
    else:
        if node.left: modifier_annee_invention(invention, date, node.left)
        if node.right: modifier_annee_invention(invention, date, node.right)




def afficher_categories_et_inventions(root):
    print(root)
    for i in liste_categories:
        print(i.afficher(),"\n")




#tests:

ajouter_categorie("Physique")
ajouter_invention("Maths", "Pendule", "Galilée", 1581)
ajouter_invention("Physique", "Stuff", "Galilée", 1231)

modifier_annee_invention("Pendule", 1602)
afficher_categories_et_inventions(racine)
