1)create env and activate - 
  first create a folder and inside that folder create a .env for django

2)install dependencies - 
Install Django and Django REST Framework:
pip install django djangorestframework djangorestframework-simplejwt psycopg2-binary django-cors-headers


3)To connect your Django project to PostgreSQL, you’ll need the psycopg2 library:
pip install psycopg2-binary

4)Run Django migrations to ensure the database is set up properly:
python manage.py makemigrations
python manage.py migrate

5)If you face any errors when run the command "python manage.py makemigrations"
  you should install the dependency that console shows

6) After successfully run the command "python manage.py migrate"
  run "python manage.py runserver"


