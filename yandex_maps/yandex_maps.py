import requests
from yandex_maps.exceptions import (
    YandexmapsAddressNotFoundException,
    YandexmapsLocationNotFoundException,
    YandexmapsInvalidApiKeyException
)


class Yandexmaps:
    def __init__(self, api_key=None, format='json', language='uz_UZ'):
        '''

        :param api_key:
        :param format:
        :param language:
        '''
        self.api_url = "https://geocode-maps.yandex.ru/1.x/"
        self.api_key = api_key
        self.format = format
        self.language = language

    def locations(self, longitude: str, latitude: str):
        '''

        :param longitude:
        :param latitude:
        :return: Узбекистан, Ташкент, сквер Амира Темура
        '''
        location = '{},{}'.format(longitude, latitude)
        data = self.request(data=location)["GeoObjectCollection"]["featureMember"]

        if not data:
            raise YandexmapsLocationNotFoundException(
                '"{},{}" not found'.format(longitude, latitude)
            )

        return data[0]["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["text"]

    def address(self, address: str):
        '''

        :param address:
        :return: ('69.279737', '41.311273')
        '''
        data = self.request(data=address)["GeoObjectCollection"]["featureMember"]

        if not data:
            raise YandexmapsAddressNotFoundException(
                '"{}" not found'.format(address)
            )

        coordinates = data[0]["GeoObject"]["Point"]["pos"]
        return tuple(coordinates.split(" "))

    def request(self, data):
        response = requests.get(
            url=self.api_url,
            params=self.params(data)
        )

        if 'error' in response.json():
            raise YandexmapsInvalidApiKeyException(
                '"{}" invalid api key'.format(self.api_key)
            )

        return response.json()["response"]

    def params(self, obj):
        data = dict(
            {
                'format': self.format,
                'geocode': obj,
                'lang': self.language
            }
        )
        if self.api_key is not None:
            data.update({'apikey': self.api_key})
        return data
