.PHONY: run-migrations
run-migrations:
	poetry run python manage.py makemigrations

.PHONY: migrate
migrate:
	poetry run python manage.py migrate

.PHONY: run-server
run-server:
	poetry run python manage.py runserver

.PHONY: superuser
superuser:
	poetry run python manage.py createsuperuser