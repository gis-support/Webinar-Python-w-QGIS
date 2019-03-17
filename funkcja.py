#coding: utf-8

#Import bibliotek
from qgis.core import *
from qgis.gui import *
from qgis.utils import iface

#Dekorator rejestrujący funkcję w kreatorze wyrażeń
@qgsfunction(args='auto', group='Webinar', usesgeometry=True)
#Właściwa funkcja przetwarzająca obiekty przestrzenne
def featureOnMap(feature, parent):
    #Pobranie zasięgu mapy
    zasieg_mapy = iface.mapCanvas().extent()
    #Stworzenie geometrii z zasięgu mapy
    geometria_mapy = QgsGeometry.fromRect( zasieg_mapy )
    #Pobranie geometrii obiektu przestrzennego
    geometria = feature.geometry()
    #Sprawdzenie czy geometria obiektu znajduje się w całości w zasięgu mapy
    return geometria.within( geometria_mapy )