import requests
from PyQt5.QtCore import QByteArray


def get_toponym(toponym_to_find):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym_to_find,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)

    if not response:
        pass

    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    toponym_coodrinates = toponym["Point"]["pos"]
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

    return get_map_image(float(toponym_longitude), float(toponym_lattitude))


def get_map_image(longitude, lattitude):
    delta = "0.05"

    map_params = {
        "ll": ",".join([str(longitude), str(lattitude)]),
        "spn": ",".join([delta, delta]),
        "l": "map"
    }

    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)

    return QByteArray(response.content)
