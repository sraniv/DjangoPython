# Django Rest Token Authentication with DJOSER

> by Venkata Bhattaram (c)

## Project setup

* install the `djoser` library, at the command line using the following command

  ```bash
  pip install djoser
  ```

* Create a database to store the user login details, here we are using MySQL, logon to the MySQL database and create the database

  ```sql
  create database djangodbauth;
  ```

* Create a **Super User** using the following at the command line, this will prompt for a password and enter a password, here Iam using `12345678`

  ```bash
  python manage.py createsuperuser --email mymail@mail.com --username admin
  ```

* Create App to demonstrate the Rest with Authentication

  ```bash
  python manage.py startapp app_auth_rest
  ```

* 

