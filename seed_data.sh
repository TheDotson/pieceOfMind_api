#!/bin/bash

rm -rf pieceOfMind_api/migrations
rm db.sqlite3
python manage.py makemigrations pieceOfMind_api
python manage.py migrate
python manage.py loaddata users
python manage.py loaddata tokens
python manage.py loaddata pieceUsers
python manage.py loaddata rooms
python manage.py loaddata collections
python manage.py loaddata items
