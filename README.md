# Django Real Estate App With Multiple Users And Databases

This project uses multiple user types and multiple databases in Django. This is a Django backend REST API using the Django REST Framework.

It has 2 databases in postgreSQL, one for **users** and other for **listings**

Steps:
-   create a virtual environment by running: python3 -m venv venv
-   then activate the virtual environment: source venv/bin/activate (MacOS) or .\venv\Scripts\activate (Windows)
-   then run the following commands:
-   pip install -r requirements.txt
-   python manage.py makemigrations
-   python manage.py migrate user --database=users
-   python manage.py migrate --database=users
-   then run the following to create a superuser:
-   python manage.py createsuperuser --database=users
-   then you can run the server by running: python manage.py runserver
