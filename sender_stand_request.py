import data
import configuration
import requests


# Создание заказа
def create_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS, json=order_body)


# Сохранение трека заказа
track_number = create_order(data.order_body).json()["track"]


# Получение заказа по треку заказа
def get_order(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDERS+str(track_number))