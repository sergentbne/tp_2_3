Travail pratique 3	420-SF2
 
Objectifs :	Concevoir une application qui met en pratique les structures de données.

Directives : 	Le travail compte pour 20% de la note finale réalisé en équipe d'au plus 2 étudiants

Date de remise : 	À déterminer



Votre tâche consiste à coder un programme Python qui permet de gérer les inventions réalisées au cours des siècles. Les inventions sont regroupées en catégories. 

•	Une catégorie est caractérisée par : le nom de la catégorie (chaine) et les inventions appartenant à cette catégorie 
•	Une invention est caractérisée par  le nom de l'invention, le nom de l'inventeur et l'année de l'invention
•	Chaque invention appartient à une et une seule catégorie
•	Les catégories seront implantées à l'aide d'un arbre binaire

Les actions à réaliser sont décrites ci-dessous (entre parenthèses les données requises) :

1-	Ajouter une catégorie (nom de la catégorie)
2-	Ajouter une invention (catégorie, nom de l'invention, nom de l'inventeur année de l'invention)
3-	Afficher les catégories et leurs inventions
4-	Modifier l'année d'une invention (nom de l'invention et la nouvelle année)
5-	Afficher les inventions d'un inventeur (nom de l'inventeur)

Vous devez prévoir les erreurs ci-dessous et afficher, le cas échéant un des messages suivants :


•	Catégorie déjà existante	(lors de l'ajout d'une catégorie)

•	Invention déjà existante 	(lors de l'ajout d'une invention, on suppose que chaque 
 invention a un nom unique)

•	Invention inexistante	(lors de la modification de l'année d'une invention)


De plus, vous devez afficher un message décrivant l'action demandée. Par exemple, après l'ajout d'une catégorie, vous affichez le message "Ajout de la catégorie : Informatique".

Pour le choix des structures de données, utilisez :

•	Un arbre binaire pour les catégories (une catégorie a pour attributs : un objet de type Node de la bibliothèque binarytree et un dictionnaire pour les inventions d'une catégorie).
 

L'exécution du programme doit se faire avec l'appel de méthodes dans le programme principal.

Exemple : 
ajouter_invention(racine, "Physique", "Pendule", "Galilée", 1581)
ajouter_invention(racine, "Informatique", "Calculateur", "Babbage", 1837)
afficher_categories_et_inventions(racine)
modifier_annee_invention(racine, "Pendule", 1602)
afficher_inventions_par_inventeur(racine, "Babbage")

