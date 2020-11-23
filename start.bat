start /wait pip install -r requirements.txt
start /wait python manage.py migrate
start /wait python generate.py
start /wait python manage.py runserver
