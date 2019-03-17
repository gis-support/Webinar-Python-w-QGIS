# Webinar _Python w QGIS_
## 18.03.2019 r.
##  Piotr Pociask, GIS Support sp. z o. o.

Materiały wykorzystane na webinarze dotyczącym wykorzystania języka Python w środowisku QGIS.
Przykładowy dane znajdują się w katalogu _projekt_, znajduje się tam również projekt QGIS _projekt_webinar.qgz_.

Pliki z kodem źródłowym:
* __makro.py__ - przybliżenie okna mapy do pierwszej warstwy na liście.
* __konsola.py__ - wyświetlenie nazwy aktualnie wybranej warstwy,
* __akcja.py__ - otworzenie przeglądarki ze stroną Wikipedii wybranego powiatu,
* __funkcja.py__ - sprawdzenie czy obiekt jest w całości wyświetlony w oknie mapy,
* __formularz.py__ - podświetlanie kolorem pola formularza atrybutów wg jego wartości,
* __aplikacja.py__ - samodzielna przeglądarka projektów QGIS. W celu uruchomienia należy ustawić zmienną _QGIS_PATH_ na katalog instalacyjny QGIS. Program należy uruchomić z konsoli _OSGeo4W Shell_:
```console
# Ustawienie python 3 jako aktywny interpreter
C:\> py3_env
# Uruchomienie aplikacji
C:\> python aplikacja.py
```