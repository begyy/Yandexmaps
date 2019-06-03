class YandexmapsException(Exception):
    pass


class YandexmapsLocationNotFoundException(YandexmapsException):
    pass


class YandexmapsAddressNotFoundException(YandexmapsException):
    pass

class YandexmapsInvalidApiKeyException(YandexmapsException):
    pass