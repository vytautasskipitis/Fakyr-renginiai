open cmd > mysite folder

venv\Scripts\activate.bat
cd mysite
py manage.py makemigrations
py manage.py migrate
py manage.py runserver

copy url > paste in browser
