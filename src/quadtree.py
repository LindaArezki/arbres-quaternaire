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
            quadtree = QuadTree.fromList(elements_quatree)
            print(elements_quatree)
            return quadtree

    @staticmethod
    def fromList(data: list) -> QuadTree:
        """ Generates a Quadtree from a list representation"""
        pass


class TkQuadTree(QuadTree):
    def paint(self):
        """ TK representation of a Quadtree"""
        pass

