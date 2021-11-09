from flask import Flask
from flask import request
import requests
import json
from ast import literal_eval
import schedule
import time



#input data as bytes
#output python object
def convertToJson(before):
    preData = before.content
    my_json = preData.decode('utf8').replace("'", '"')
    data = json.loads(my_json)
    data = data["Data"]
    return data

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

#create objects according to category
def prepareDataByCategory(myCategory):
    categoryList = data["categoriesList"]
    category_dish_list = []
    toReturn = {}
    for category in categoryList:

        if category["categoryName"] == myCategory:
            category_dish_list = category["dishList"]
    if (len(category_dish_list) > 0):
        itemList = []
        for dish in category_dish_list:
            myItem = {
                "id": dish["dishId"],
                "name": dish["dishName"],
                "description": dish["dishDescription"],
                "price": dish["dishPrice"],
            }
            itemList.append(myItem)
        toReturn["Data"] = itemList
        return toReturn


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





#find item by category and id
def getItemById(page_id, my_category):
    pageid = page_id
    all_items = mappedData[my_category]
    toReturn = {}
    for item in all_items:
        toReturn = item
        print("item id: " ,type(item["id"]))
        print(type(pageid))
        if str(item["id"]) == pageid:
            print("in ifffff")
            return toReturn
    return toReturn




# return total amount of order
def returnTotal():
    total_price = 0
    my_json = request.data.decode('utf8').replace("'", '"')

    data = json.loads(my_json)
    for key, value in data.items():
        item_list_by_category = literal_eval(value)
        for id_item_order in item_list_by_category:
            for item in mappedData[key]:
                if id_item_order == item["id"]:
                    total_price += item["price"]

    return str({"price": total_price})



app = Flask(__name__)