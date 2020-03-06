#!/usr/bin/python3

#
# Ce programme analyse une image integrant un code barre 
# au format pdf417, lit les donnees puis modifie la classe 
# de de economie vers business, puis regenere un code barre.
#
# Ne pas utiliser en prod \o/
#

from plane import Plane
import sys

def main(filepath):
    airbus = Plane(filepath)
    airbus.fly()

if __name__ == '__main__':
    main(sys.argv[1])