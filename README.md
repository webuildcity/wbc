BuergerbautStadt
================
1) Python und Django installieren: https://docs.djangoproject.com/en/1.4/intro/install/
2) Repository in einem beliebigen Ordner clonen
3) gehe in <euer Pfad>/bbs/bbs und kopiere die Datei settings.sample.py in den gleichen Ordner und nenne die Kopie settings.py
4) Öffne settings.py in einem Texteditor und ändert in Zeile 4 die Variable so, dass da Euer Dateipfad drinsteht. Speichern und Schließen
5) Eine Konsole öffnen und per cd <Euer Pfad>/bbs in den Ordner bbs wechseln in dem die manage.py liegt
6) in der Konsole python manage.py runserver ausführen 
7) Browser öffnen und in die URL http://localhost:8000/ aufrufen -> Es sollte eine Berlinkarte zu sehen sein
8) über http://localhost:8000/admin/ könnt ihr Euch einloggen (User: admin, pw: admin). Dort seht ihr die Tabelle Projects -> Wenn ihr darauf klickt kann man neue Bauvorhaben hinzufügen