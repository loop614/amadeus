Amadeus API consumer in One day
- without using the amadeus package

## Requirements
- docker (with compose)

## QUICK START
```console
docker compose up

docker compose exec web python manage.py makemigrations &&
docker compose exec web python manage.py migrate --noinput
```
[visit] (http://localhost:8000/flights/?departure_iata=HSV&destination_iata=BHM&outgoing_date=2023-10-10&return_date=2023-11-10&round_trip=1&passenger_count=1&currency=EUR) 

## TODOs
- response to match when reading from db and when fetching fresh
- html
- remove unused files
- run pre-commit
- add even more caching
