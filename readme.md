## Commands for Initial setup <br>


&ensp;__Pre Setup__ <br>

    1. python3 -m venv venv (Creation of virtual environment)
    2. source venv/bin/activate  


## Installing requirement

    pip install -r requirements.txt 

## Moving into specific directory

    cd 'microservice to display all trains' or 'number management http service'

## Running the server

    python3 app.py


# First Question
## Get All Trains (Sorted)

### Request

`POST /trains/all`

    curl --location --request GET 'http://localhost:8080/trains/all' \
    --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTA3OTg4MjAsImNvbXBhbnlOYW1lIjoiU3JpIGtyaXNobmEgQ29sbGVnZSBvZiBFbmdpbmVlcmluZyBhbmQgVGVjaG5vbG9neSIsImNsaWVudElEIjoiMWQ3ZDkyYmQtYWExMi00NzhiLWI0ZmEtNzI4MzA4NWMzN2NlIiwib3duZXJOYW1lIjoiIiwib3duZXJFbWFpbCI6IiIsInJvbGxObyI6IjIwZXVjczEyNSJ9.OEap5oFT8TSbltc0fQ21-6IUjqJ2m9Oz-az24stV4S4'

### Response

![Response Image](./microservice%20to%20display%20all%20trains/library/response.png)


# Second Question
## Number Management

### Request

`GET /number/management?url=http://20.244.56.144/numbers/primes&url=http://20.244.56.144/numbers/odd`

    curl --location --request GET 'http://localhost:8080/number/management?url=http://20.244.56.144/numbers/primes&url=http://20.244.56.144/numbers/odd'


### Response Image

![Response Image](./number%20management%20http%20service/library/response.png)