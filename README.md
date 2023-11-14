## Exercice : Arbre quaternaire
Dans le cadre de mon bachelor CDA : Concepteur Développeur d'Applications il fallait réaliser un QuadTree.

#Qu'est- ce qu'un QuadTree
Un quadtree ou arbre quaternaire (arbre Q) est une structure de données de type arbre dans laquelle chaque nœud a quatre fils. Les quadtrees sont le plus souvent utilisés pour partitionner un espace bidimensionnel en le subdivisant récursivement en quatre nœuds. 

![img.png](files/quadtree.png)

## Proposition d'implementation : Arbre quaternaire
    Pour essayer de répondre à cet exercice j'ai procedée par étapes :
    1) Initialisation d'un objet QuadTree
    2) Renommage et rédaction de la méthode from_file qui ouvre un fichier avec la representation d'une liste qui correspond à un Quadtree. (Test d'un print pour verifier les élements récupérés)
    3) Renommage et rédaction de la méthode from_list qui récupére chaque élements du quadtree et qui les mets dans des nouvelles variables pour générer un quadtree.(Test d'un print pour verifier les élementsrécupérés de chaque variables)
    4) Rédaction de la méthode depth qui récupère le nombre de lignes/noeuds soit la profondeur du Quadtree en fonction du fichier récupéré. (Test d'un print pour verifier la profondeur du fichier)
    5) Vérifier les tests pytest en ajustant le nom des méthodes et en changeant d'emplacement les fichiers.
    6) Ajout d'une nouvelle méthode __str__ permettant de récupérer sous forme de liste les élements d'un QuadTree afin d'ajouter de nouveaux tests pytest qui vérifie les lignes récupérés.
    
## Structure du projet
    - `src/quadtree.py` : Implémentation de la classe QuadTree.
    - `tests/test_quadtree.py` : Tests unitaires.

## Récupération du projet
    Récupération du projet sur ce depôt sur le gitlab de docusland :
          https://gitlab.com/docusland-courses/python/python-exercices-ludiques/-/tree/arbre-quaternaire?ref_type=heads
    



