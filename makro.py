#coding: utf-8

#Wymagane importy
from qgis.core import QgsProject
from qgis.utils import iface

#Funkcja uruchamiana przy otwieraniu projektu
def openProject():
    #Pobranie pierwszej warstwy w legendzie
    warstwa = QgsProject.instance().layerTreeRoot().children()[0].layer()
    #Zasięg warstwy
    zasieg = warstwa.extent()
    #Ustawienie zasięgu mapy do zasięgu warstwy
    iface.mapCanvas().setExtent( zasieg )
    #Odświeżenie warstwy
    warstwa.triggerRepaint()