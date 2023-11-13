from __future__ import annotations
import json


class QuadTree:
    """
        Une classe représentant un Quadtree
        ...
        Attributes
        ----------
            - hg (bool | QuadTree): élements en haut à gauche.
            - hd (bool | QuadTree): élements en haut à droite.
            - bd (bool | QuadTree): élements en bas à droite.
            - bg (bool | QuadTree): élements en bas à gauche.

        Methods
        -------
              __init__(self, hg: bool | QuadTree, hd: bool | QuadTree, bd: bool | QuadTree, bg: bool | QuadTree):
                    Initialisateur d'un objet QuadTree.
              depth(self) -> int:
                    Défini la longueur du QuadTree, le nombre de lignes/noeuds
              from_file(filename: str) -> QuadTree:
                     Ouvre un fichier donné qui contient la représentation textuelle d'une liste.
              from_list(data: list) -> QuadTree:
                    Génère le Quadtree à partir de la liste qui la représente en retournant un objet QuadTree.
              __str__(self):
                    Génère le Quadtree à partir de la liste qui la représente en retournant une liste
        """
    NB_NOEUDS: int = 4

    def __init__(self, hg: bool | QuadTree, hd: bool | QuadTree, bd: bool | QuadTree, bg: bool | QuadTree):
        """
             Initialisateur d'un objet QuadTree.
                 Parameters:
                             - hg (bool | QuadTree): élements en haut à gauche.
                             - hd (bool | QuadTree): élements en haut à droite.
                             - bd (bool | QuadTree): élements en bas à droite.
                             - bg (bool | QuadTree): élements en bas à gauche.
        """
        self.profondeur = 0
        self.__hg = hg  # en haut à gauche
        self.__hd = hd  # en haut à droite
        self.__bd = bd  # en bas à droite
        self.__bg = bg  # en bas à gauche

    @property
    def depth(self) -> int:
        """
            Défini la longueur du QuadTree, le nombre de lignes/noeuds
                Returns:
                           Une variable du Quadtree.
        """
        return self.profondeur

    @staticmethod
    def from_file(filename: str) -> QuadTree:
        """
            Ouvre un fichier donné qui contient la représentation textuelle d'une liste.
               Parameters:
                          - filename (str): Le nom du fichier à ouvrir.
               Returns:
                          Un objet QuadTree généré à partir du contenu du fichier.
        """
        with open(filename, "r", encoding="utf-8") as fichier:
            lire_fichier = fichier.read()
            elements_quatree = json.loads(lire_fichier)
            lignes_quatree = len(lire_fichier.replace("]", "").strip("[").split())
            quadtree = QuadTree.from_list(elements_quatree)
            quadtree.profondeur = lignes_quatree
            return quadtree

    @staticmethod
    def from_list(data: list) -> QuadTree:
        """
             Génère le Quadtree à partir de la liste qui la représente en retournant un objet QuadTree.
                Parameters:
                            - data (list): Liste représentant les élements d'un QuadTree.
                Returns:
                            Un objet QuadTree généré à partir de la liste.
        """
        haut_a_gauche = data[0]
        haut_a_droite = data[1]
        bas_a_droite = data[2]
        bas_a_gauche = data[3]
        new_quadtree = QuadTree(haut_a_gauche, haut_a_droite, bas_a_droite, bas_a_gauche)
        return new_quadtree

    def __str__(self):
        """
             Génère le Quadtree à partir de la liste qui la représente en retournant une liste
                Returns:
                            La liste de tous les éléments du Quadtree.
        """
        return f"[{self.__hg}, {self.__hd}, {self.__bd}, {self.__bg}]"


class TkQuadTree(QuadTree):
    def paint(self):
        """ TK representation of a Quadtree"""
        pass
