
migrate:
	python take5/manage.py makemigrations
	python take5/manage.py migrate


deploy:
	python take5/manage.py runserver localhost:8080
