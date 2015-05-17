
## Setup
* Install python, pip, virtualenv
* Install postgresql
  * brew install postgresql
  * export DATABASE_URL=postgres:///$(whoami)
* Clone the repo
* Create a virtualenv
  * virtualenv venv
  * source venv/bin/activate
  * pip install -r requirements.txt
* Create database tables
  * python manage.py migrate 

## Start server
 python manage.py runserver
