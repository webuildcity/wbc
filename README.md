BuergerbautStadt
================

[http://buergerbautstadt.de][bbs] - Finde geplante Bauvorhaben in deinem Kiez.

## Starthilfe

1. Python und [Django installieren][django-install].
2. Repository in einem beliebigen Ordner clonen.
3. Gehe in `euer/pfad/bbs/bbs` und kopiere die Datei `default.local.py` in den gleichen Ordner und nenne die Kopie `local.py`.
4. Öffne `local.py` in einem Texteditor und ändert die Werte für den Datenbankadapter.
5. Eine Konsole öffnen und per `cd euer/pfad/bbs` in den Ordner `bbs` wechseln,in dem die `manage.py` liegt.
6. In der Konsole `python manage.py syncdb` ausführen und *User* + *Passwort* angeben. In der Konsole `python manage.py runserver` ausführen. 
8. Browser öffnen und in die URL [http://localhost:8000/][bbs-home] aufrufen -> Es sollte eine Berlin-Karte zu sehen sein.
9. Über [http://localhost:8000/admin/][bbs-admin] könnt ihr Euch einloggen. Dort seht ihr die Tabelle *Projects* -> Wenn ihr darauf klickt, kann man neue Bauvorhaben hinzufügen.


[bbs]: http://buergerbautstadt.de
[django-install]: https://docs.djangoproject.com/en/1.4/intro/install/
[bbs-home]: http://localhost:8000/
[bbs-admin]: http://localhost:8000/admin/
