from categorie import *
from invention import *
from binarytree import Node

racine = categorie("Racine")



def ajouter_categorie(element,node=racine):
    global racine
    if node.value < element:
        if node.right: return ajouter_categorie(element, node.right)
        else: 
            node.right = categorie(element)
            return node.right
        
    elif node.value > element:
        if node.left: return ajouter_categorie(element, node.left)
        else: 
            node.left = categorie(element)
            return node.left
        
    return node




def ajouter_invention(nom_cat, nom, inventeur, date):
    ajouter_categorie(nom_cat).ajouter_invention(Invention(nom, inventeur, date))

def modifier_annee_invention(invention, date, node = racine):
    global racine
    if node:
        inventions_dict = node.get_inventions()
        if invention in inventions_dict:
            inventions_dict[invention].set_annee(date)
        else:
            if node.left: modifier_annee_invention(invention, date, node.left)
            if node.right: modifier_annee_invention(invention, date, node.right)




def afficher_categories_et_inventions(node = racine):
    if node: 
        print(node.afficher(),"\n")
        afficher_categories_et_inventions(node.left)
        afficher_categories_et_inventions(node.right)


def afficher_inventions_par_inventeur(inventeur, node = racine):
    if node:
        if node == racine:
            print("Inventions de",inventeur,":")
        inventions_dict = node.get_inventions()
        for i in node.get_inventions():
            if inventions_dict[i].get_inventeur() == inventeur:
                print(inventions_dict[i])
                
        afficher_inventions_par_inventeur(inventeur, node.left)
        afficher_inventions_par_inventeur(inventeur, node.right)
        



#tests:
#ajouter inventions ajoute automatiquement la categorie si elle n'est pas presente

ajouter_invention("Maths", "Pendule", "Galilée", 1581)
ajouter_invention("Informatique", "Calculateur", "Babbage", 1837)
ajouter_categorie("Physique")
ajouter_invention("Physique", "Stuff", "Galilée", 1231)

modifier_annee_invention("Pendule", 1602)

print(racine)

afficher_categories_et_inventions()

afficher_inventions_par_inventeur("Babbage")
