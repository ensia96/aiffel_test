install:
	pip install -U -r requirements.txt

env:
	direnv allow

run:
	python manage.py runserver

migrate:
	python manage.py makemigrations && python manage.py migrate

test:
	python manage.py test
