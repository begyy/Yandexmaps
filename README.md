# Yandexmaps
[![Downloads](https://pepy.tech/badge/yandexmaps)](https://pepy.tech/project/yandexmaps)
![Python application](https://github.com/begyy/Yandexmaps/workflows/Python%20application/badge.svg)
````
pip install requests
pip install yandexmaps
````

# Example

```
from yandex_maps import Yandexmaps
yandex = Yandexmaps()
yandex.address('Узбекистан, Ташкент, сквер Амира Темура')
>>> ('69.279737', '41.311273')

yandex.locations(longitude='69.279737', latitude='41.311273')
>>> Oʻzbekiston, Toshkent, Amir Temur xiyoboni
```

```
from yandex_maps import Yandexmaps
Yandexmaps(language='ru_RU',api_key='token').locations(longitude='69.279737', latitude='41.311273')
>>> Узбекистан, Ташкент, сквер Амира Темура

```
