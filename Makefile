AMADEUSPYTHON := docker compose exec amadeus_python
AMADEUSPYTHONMANAGE := docker compose exec amadeus_python python manage.py

build:
	docker compose build --no-cache
	docker compose up --remove-orphans

migrate:
	$(AMADEUSPYTHONMANAGE) makemigrations
	$(AMADEUSPYTHONMANAGE) migrate --noinput
