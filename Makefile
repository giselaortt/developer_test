
migrate:
	python manage.py makemigrations
	python manage.py migrate


deploy:
	python manage.py runserver localhost:8080
