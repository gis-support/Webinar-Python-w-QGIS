#coding: utf-8

#Import niezbędnych klas
from qgis.PyQt.QtCore import QUrl
from qgis.PyQt.QtWebKitWidgets import QWebView

#Pobranie wartości z tabeli atrybutów
nazwa = '[%jpt_nazwa_%]'
#Sformatowanie adresu do strony Wikipedii
url = 'https://pl.wikipedia.org/wiki/{}'.format( nazwa )
#Stworzenie przeglądarki
przegladarka = QWebView()
#Ustawienie rozmiaru okna przeglądarki
przegladarka.resize( 1200, 800 )
#Załadowanie strony w przeglądarce
przegladarka.load( QUrl( url ) )
#Wyświetlenie okna przeglądarki
przegladarka.show()