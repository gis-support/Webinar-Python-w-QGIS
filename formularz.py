# -*- coding: utf-8 -*-

from qgis.PyQt.QtWidgets import QWidget

def form_open(dialog, layer, feature):
    #Wyszukanie kontrolki
    capacity = dialog.findChild(QWidget, "capacity")
    #Kolor podświetlenia
    try:
        color = color_from_value(feature['capacity'])
    except:
        #W przypadku błędu kończymy działanie funkcji
        return
    #Ustawienie stylu
    capacity.setStyleSheet("background-color: {};".format( color ) )

def color_from_value(value):
    #Zwrócenie koloru w zależności od podanej wartości
    value = int(value)
    if value<=5:
        return 'red'
    elif value<=15:
        return 'yellow'
    else:
        return 'green'
