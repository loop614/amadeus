### Django App Amadeus API consumer with Postgres

### Requirements
- docker (with compose)
- make

### QUICK START
```console
$ docker compose up
$ make migrate # while composer running
```
- [open localhost](http://localhost:12345/flights/?departure_iata=HSV&destination_iata=BHM&outgoing_date=2023-10-10&return_date=2023-11-10&round_trip=1&passenger_count=1&currency=EUR)

### Status
- since we lost the amadeus API keys, only edit dates in link above, only use HSV and BHM iatas
- one response is from mocked api, next from database
