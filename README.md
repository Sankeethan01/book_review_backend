1) create env and activate - 
  first create a folder named "backend" and open it in VS code 

2) create env and install dependencies - 
 run command inside "backend" folder - " Install Django and Django REST Framework:
pip install django djangorestframework djangorestframework-simplejwt psycopg2-binary django-cors-headers
"
3) then inside the "backend" folder clone the backend repository - " git clone backend-url "bookreview_backend "

  folder structure

![Screenshot 2025-02-02 173253](https://github.com/user-attachments/assets/5f5d230e-9898-417a-a544-efebccbe9ebf)



3) To connect your Django project to PostgreSQL, you’ll need the psycopg2 library:
 "pip install psycopg2-binary"

4) You are required to install PostgreSQL for database
 and create database named "book_review_db"
   then you need to set your password for pg admin in settings.py

Then go to direct to "bookreview_backend " folder run migrations

![Screenshot 2025-02-02 174356](https://github.com/user-attachments/assets/3bf30734-89c2-49e1-a2ce-fd4e7fb17f78)


5) Run Django migrations to ensure the database is set up properly:
 "python manage.py makemigrations" then
 "python manage.py migrate"

5)If you face any errors when run the command "python manage.py makemigrations"
  you should install the dependency that console shows

6) After successfully run the command "python manage.py migrate"
  run "python manage.py runserver"


