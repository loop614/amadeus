AMADEUSPYTHON := docker compose exec amadeus_python

build:
	docker compose build --no-cache
	docker compose up --remove-orphans
