# CarDjangoCRUD

### Virtual Environments 
`python -m venv py3EnvCarDjangoCRUD`

### Activating a Virtual Environment
* Mac/Linux: `source py3EnvCarDjangoCRUD/bin/activate`

* Windows git bash `source py3EnvCarDjangoCRUD/Scripts/activate`

### Django Virtual Environment
pip3 install Django==3
pip3 list
____________
### 1- Creating a Django Project
`(djangoPy3Env) > django-admin startproject your_project_name_here`
### 2- run for initializing <p>localhost:8000</p>
`(djangoPy3Env) your_project_name_here> python3 manage.py runserver`
### 3- create App
* `(djangoPy3Env) your_project_name_here> mkdir apps`
* `(djangoPy3Env) apps> python3 ../manage.py startapp your_app_name_here`
### 4- create urls.py for the App
`(djangoPy3Env) your_app_name_here> touch urls.py`
### 5- your_project_name_here/your_project_name_here/settings.py
`INSTALLED_APPS = [
       'apps.your_app_name_here', # added this line. Don't forget the comma!!]`
### 6- ORM and Session
 * `> python3 manage.py makemigrations`
 * `> python3 manage.py migrate`
