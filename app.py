from flask import Flask
from flask import request
import requests
import json
from ast import literal_eval
import schedule
import time
from logic import *

#get data from api
def getData():
    print('get data is called')
    url = 'https://www.10bis.co.il/NextApi/GetRestaurantMenu?culture=en&uiCulture=en&restaurantId=19156&deliveryMethod=pickup'
    headers = {'Accept': 'application/json'}
    response = requests.get(url, headers=headers)
    global data
    data = convertToJson(response)
    return data


def updateData(numOfDays):
    return schedule.every(numOfDays).days.do(getData());



# fetching data
url = 'https://www.10bis.co.il/NextApi/GetRestaurantMenu?culture=en&uiCulture=en&restaurantId=19156&deliveryMethod=pickup'
headers = {'Accept': 'application/json'}
response = requests.get(url, headers=headers)
data = convertToJson(response)


def prepareAllData():
    global drinksData
    global pizzasData
    global dessertsData
    drinksData = prepareDataByCategory("Drinks")
    pizzasData = prepareDataByCategory("Pizzas")
    dessertsData = prepareDataByCategory("Desserts")
    global mappedData
    mappedData = {
        "drinks": drinksData["Data"],
        "pizzas": pizzasData["Data"],
        "desserts": dessertsData["Data"],
    }


#send out to sorting
drinksData = prepareDataByCategory("Drinks")
pizzasData = prepareDataByCategory("Pizzas")
dessertsData = prepareDataByCategory("Desserts")

#global value of all mapped data
mappedData = {
    "drinks": drinksData["Data"],
    "pizzas": pizzasData["Data"],
    "desserts": dessertsData["Data"],
}

def dataFetch():
    schedule.every(1).days.do(getData());
    while 1:
        schedule.run_pending()
        time.sleep(1000)


app = Flask(__name__)




@app.route('/drinks')
def get_drinks():
    return drinksData


@app.route('/drinks/<page_id>')
def drinkById(page_id):
    return getItemById(page_id, "drinks")


@app.route('/pizzas')
def get_pizzas():
    return pizzasData


@app.route('/pizzas/<page_id>')
def pizzaById(page_id):
    return getItemById(page_id, "pizzas")


@app.route('/desserts')
def get_desserts():
    return dessertsData


@app.route('/desserts/<page_id>')
def dessertById(page_id):
    return getItemById(page_id, "desserts")


@app.route('/order',methods=['GET', 'POST'])
def executeOrder():
    if request.method == 'POST':
        return returnTotal()

    return 0


if __name__ == '__main__':
    app.run()

