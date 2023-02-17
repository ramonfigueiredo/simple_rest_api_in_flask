# Simple REST API in Flask

## Installation and setup

1) Create python virtual environment

```
python3 -m venv .venv
```

2) Activate python virtual environment

```
source ./.venv/bin/activate
```

3) Install python dependencies

* Upgrade pip

```
python3 -m pip install --upgrade pip
```

* Install python dependencies 
```
pip install -r requirements.txt
```

4) Export 'FLASK' environment variables.

```
export FLASK_APP=application.py
export FLASK_DEBUG=1
```

5) Populate database

* Open Flask shell 

```
flask shell
```

* Run the commands

```
from application import db
db.create_all()

drink = Drink(name="Grape Soda", description="Taste like grapes")
db.session.add(drink)

drink = Drink(name="Cherry Soda", description="Taste like cherry")
db.session.add(drink)

db.session.commit()
```

* Exit Flask shell 
```
exit()
```

## Running the API
```
flask run
```

## Testing the API

The api can be tests using ```curl``` or tools like [Postman](https://www.postman.com/).

API-URL: http://127.0.0.1:5000
```
curl http://127.0.0.1:5000
```

Output:
```
Simple REST API in Flask
```

1) [GET] Endpoint to list all drinks: **API-URL/drinks**
```
curl http://127.0.0.1:5000/drinks
```

Output:

```
{
  "drinks": [
    {
      "description": "Taste like grapes",
      "name": "Grape Soda"
    },
    {
      "description": "Taste like cherry",
      "name": "Cherry Soda"
    }
  ]
}
```

2) [GET] Endpoint to get one drink using its ID: **API-URL/drinks/ID**

```
curl http://127.0.0.1:5000/drinks/1
```

Output:

```
{
  "description": "Taste like grapes",
  "name": "Grape Soda"
}
```

3) [POST] Endpoint to create a drink: POST **API-URL/drinks**

```
curl -X POST http://localhost:5000/drinks/ -H "Content-Type: application/json" -d '{"name": "Coke", "description": "Coca-Cola drink"}'  
```

Output:

```
{
  "id": 3
}
```

4) [DELETE] Endpoint to create a drink: DELETE **API-URL/drinks/ID**

```
curl -X "DELETE" http://127.0.0.1:5000/drinks/3
```