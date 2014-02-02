#!/bin/bash

if [ ! -f "bbs/settings.py" ]; then
    echo "Error: not in the root directory of the django project."
fi

./manage.py collectstatic --noinput
sudo service apache2 reload