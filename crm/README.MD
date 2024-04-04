# Guideline for Building a CRM with Django Framework

## Installation

1. Setup the Virtual Environment `python -3 venv [name]`
2. Activate the virtual environment `[name]\scripts\activate`
3. Install 
            `python -m pip install Django`
            `python -m pip install --upgrade pip`
            `python -m pip install Wheel`
            `python -m pip install mysql-connector`
            `python -m pip install mysql-connector-python`

### Start Project with Django
1. Run on terminal
            `django-admin startproject Your_Project_Name`
2. Navigate to the ProjectName directory
            `python manage.py startapp Your_App_Name`

### Navigate Back to ProjectName directory
1. Under settings.py file, go to INSTALLED_APPS, add `Your_App_Name`

## Database
- [x] Under settings.py file, navigate to DATABASES iff, you need to change the database to MySQL or POSTgre.

For MySQL, insert the following and delete what's there.

        `DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME':'Your_db_Name',
                'USER':'root',
                'PASSWORD':'password123',
                'HOST':'localhost',
                'PORT':'3306',
            }
        }`

### Create a Database
Navigate to the `Your_Project_Name` folder directory.
* Ensure to list items of the directory.
* Type `dir /b` on terminal, for windows. Ensure that on the listed items, `manage.py` is there.
* Type `type nul > Your_Database_Name.py` on the terminal to create a new python file for databases

Inside the `Your_Database_Name.py`, type the following code;

        import mysql.connector

        # Connect to MySQL server
        dataBase = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='password123',
            auth_plugin='mysql_native_password')

        # Prepare a cursor
        cursorObject = dataBase.cursor()

        # Create a database 
        cursorObject.execute("CREATE DATABASE Your_db_Name")

        print("All Done!")

* On the Terminal, type `python Your_Database_Name.py`. You should see **All Done!** printed out.
* Incase of an error with auth, check if **`auth_plugin='mysql_native_password`** is set to native as I have.

Navigate to the `Your_Project_Name` folder directory.
* Ensure to list items of the directory.
* Type `dir /b` on terminal, for windows. Ensure that on the listed items, `manage.py` is there.
* Then type `python manage.py migrate` on the terminal

All Done! We have created our database.

## Building the Application with Django









