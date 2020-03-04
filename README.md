

## Setup

### Local development

Setup Linux packages
```shell script
sudo apt install postgresql
```
Create databases:
```shell script
sudo -u postgres createuser krynegger --createdb --createrole --pwprompt --login
sudo -u postgres createdb krynegger_database --owner=krynegger
```

Setup and activate virtual environment:
```shell script
virtualenv --python=/usr/bin/python3.7 .env
source .env/bin/activate
```

Install python requirements:

```shell script
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

Install:
```shell script
pip install -r requirements.txt
python manage.py makemigrations
python manage.py createsuperuser
python manage.py runserver
```

### Testing

```shell script
tox
```
