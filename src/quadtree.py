from __future__ import annotations

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
    def fromFile(filename: str) -> QuadTree:
        """ Open a given file, containing a textual representation of a list"""
        pass

    @staticmethod
    def fromList(data: list) -> QuadTree:
        """ Generates a Quadtree from a list representation"""
        pass


class TkQuadTree(QuadTree):
    def paint(self):
        """ TK representation of a Quadtree"""
        pass