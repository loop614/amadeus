Example Django App with Postgres cache and integrations
Amadeus API consumer

## Requirements
- docker (with compose)

## QUICK START
```console
docker compose up

docker compose exec amadeus_python python manage.py makemigrations &&
docker compose exec amadeus_python python manage.py migrate --noinput
```
visit 
- http://localhost:12345/flights/?departure_iata=HSV&destination_iata=BHM&outgoing_date=2023-10-10&return_date=2023-11-10&round_trip=1&passenger_count=1&currency=EUR

## Notice
- since we lost the amadeus API keys, only edit dates in link above
- one response should be from api, next from database

## TODOs
- response to match when reading from db and when fetching fresh
- remove unused files
- run pre-commit
- add even more caching
