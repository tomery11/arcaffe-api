Hi!
This project is a reconstruction of a 10bis api.
it returns items from arrcaffe's menu

To run the project in the root folder run the following command:
'flask run'

THESE ARE THE API'S WE SUPPORT
GET /drinks - Returns the id, name, description and price of all drinks
GET /drink/<id> - Returns id, name, description and price of a drink
GET /pizzas - Returns the id, name, description and price of all pizzas
GET /pizza/<id> - Returns id, name, description and price of a pizza
GET /desserts - Returns the id, name, description and price of all desserts
GET /dessert/<id> - Returns id, name, description and price of a dessert
POST /order - receives an order and returns its total price.
body of object must look like this:

{
    "drinks": "[2055846,2055846]",
    "desserts": "[2055836,2055836,2055836]",
    "pizzas": "[2055833,2055833]"
}


to run tests
first run server: flask run
and then run in root folder in another terminal
pytest tests.py
