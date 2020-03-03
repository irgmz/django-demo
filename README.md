# age-verification

## set up instructions

pip install virtualenv
virtualenv -p python2 env
source env/bin/activate

pip install django==1.11.24
pip install rollbar

python manage.py runserver
