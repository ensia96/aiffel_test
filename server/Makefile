install:
	pip install -U -r requirements.txt

env:
	direnv allow

run:
	python manage.py runserver

shell:
	python manage.py shell

db:
	sqlite3 db.sqlite3

migrate:
	python manage.py makemigrations && python manage.py migrate

test:
	python manage.py test
