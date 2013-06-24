#!/bin/bash

if [ ! -f "manage.py" ]; then
    echo "Error: not in the root directory of the django project."
fi

./manage.py dumpdata projekte > data/projekte.json
./manage.py dumpdata news > data/news.json
