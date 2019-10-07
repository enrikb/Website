# GreenClothaWay

## How to run the website ?

First of all, you will need to install the latest version of Python [here](https://www.python.org/downloads/).

When Python is installed, open the Terminal and install the latest version of Django:

```
pip install django
```

You must then install PostgreSQL [here](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads).
If you are asked to install pgAdmin 4, do it, we will need it.

Open pgAdmin 4 and choose the default server named "PostgreSQL 11",
then you can create a new role named "admin" with all rights (superadmin).

Finally you'll need to create the "greenclothaway" database with "admin" as owner.

Reopen the terminal and install pthe psycopg2 package (it allows you to use the database you configured).
```
pip install django psycopg2
```

You can then clone this repo and go into it with:

```
cd Website/
```

To generate the database and needed tables, use this command:

```
python manage.py migrate
```

Finally you must execute this command:

```
python manage.py runserver
```

The default port is 8000, so you can access to the website with the address:

```
http://localhost:8000
or
http://127.0.0.1:8000
```

Have fun!
