from __future__ import annotations
import json

class QuadTree:

    NB_NOEUDS: int = 4

    def __init__(self, hg: bool | QuadTree, hd: bool | QuadTree, bd: bool | QuadTree, bg: bool | QuadTree):
        """ Initialisateur d'un objet QuadTree"""
        self.profondeur = 0
        self.__hg = hg  # en haut à gauche
        self.__hd = hd  # en haut à droite
        self.__bd = bd  # en bas à droite
        self.__bg = bg  # en bas à gauche

    @property
    def depth(self) -> int:
        """ Recursion depth of the quadtree"""
        return 1

    @staticmethod
    def from_file(filename: str) -> QuadTree:
        """Ouvre un fichier donnée qui contient la représentation textuelle d'une liste"""
        with open(filename, "r", encoding="utf-8") as fichier:
            lire_fichier = fichier.read()
            elements_quatree = json.loads(lire_fichier)
            quadtree = QuadTree.from_list(elements_quatree)
            return quadtree

    @staticmethod
    def from_list(data: list) -> QuadTree:
        """Génère le Quadtree à partir de la liste qui la représente en retournant un objet QuadTree"""
        haut_a_gauche = data[0]
        haut_a_droite = data[1]
        bas_a_droite = data[2]
        bas_a_gauche = data[3]
        print("les lignes sont récupérés :  haut à droite = ", haut_a_droite, " bas_a_gauche = ", bas_a_gauche,
              " haut_a_gauche = ", haut_a_gauche, " bas_a_droitee = ", bas_a_droite)
        new_quadtree = QuadTree(haut_a_gauche, haut_a_droite, bas_a_droite, bas_a_gauche)
        return new_quadtree


class TkQuadTree(QuadTree):
    def paint(self):
        """ TK representation of a Quadtree"""
        pass

