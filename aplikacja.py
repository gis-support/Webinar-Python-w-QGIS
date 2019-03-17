# coding: utf-8

"""
Samodzielna przeglądarka projektów QGIS.
Przykład przygotowany na Webinar 'Python w QGIS' 18.03.2019

Autor: Piotr Pociask, GIS Support
Licencja: MIT
"""

import sys
import os
#Katlog instalacyjny QGIS
QGIS_PATH = r'C:\OSGeo4W\apps\qgis'
#Ustawienie ścieżek
sys.path.append( os.path.join(QGIS_PATH, 'python') )
os.environ['PATH'] = '{};{};{}'.format(os.path.join(QGIS_PATH, 'bin'), os.path.join(QGIS_PATH, '../qt5/bin'), os.environ['PATH'])
os.environ['QT_PLUGIN_PATH'] = '{};{}'.format(os.path.join(QGIS_PATH, 'qtplugins'), os.path.join(QGIS_PATH, '../qt5/plugins'))
os.environ['QGIS_PREFIX_PATH'] = QGIS_PATH

#Importy
from qgis.core import *
from qgis.gui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

QgsApplication.setPrefixPath(QGIS_PATH, True)

def loadProject( map ):
    """ Załadowanie danych z projektu """
    def layerLoaded( layer, node ):
        #Zapamiętujemy warstwy z projektu w formie listy
        layers.append( layer )
    #Wybranie pliku
    path = QFileDialog.getOpenFileName( caption='Wybierz projekt QGIS...', filter='Projekt QGIS (*.qgs *.qgz)' )[0]
    if not path:
        return
    #Lista warstw
    layers = []
    #Nowy projekt
    project = QgsProject.instance()
    #Przygotowanie do rejestracji warstw na mapie
    project.readMapLayer.connect( layerLoaded )
    #Odczyt pliku projektu
    project.read(path)
    project.readMapLayer.disconnect( layerLoaded )
    #Dodane warstw do mapy
    map.setLayers( layers )
    #Przybliżenie do pełnego widoku
    map.zoomToFullExtent()

def main():
    #Stworzenie aplikacji QGIS
    app = QgsApplication([], True)
    app.initQgis()
    #Okno dialogowe
    dialog = QDialog(flags=Qt.Window)
    dialog.setWindowTitle( 'Przeglądarka GIS' )
    dialog.resize(1000, 800)
    layout = QGridLayout(dialog)
    #Przyciski
    btnLoadProject = QPushButton(dialog)
    btnLoadProject.setText( 'Otwórz projekt' )
    btnZoomExtent = QPushButton(dialog)
    btnZoomExtent.setText( 'Powiększ do warstw' )
    #Mapa
    map = QgsMapCanvas(dialog)
    #Sygnały
    btnLoadProject.clicked.connect( lambda: loadProject(map) )
    btnZoomExtent.clicked.connect( map.zoomToFullExtent )
    #Dodanie widżetów do okna dialogowego
    layout.addWidget(btnLoadProject, 0, 0)
    layout.addWidget(btnZoomExtent, 0, 1)
    layout.addWidget(map, 1, 0, 1, 2)
    #Wyświetlenie okna dialogowego
    dialog.show()
    #Pętla zdarzeń
    sys.exit( app.exec_() )
    app.exitQgis()

if __name__=='__main__':
    #Uruchomienie aplikacji
    main()
