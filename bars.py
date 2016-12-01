import json
import math


def load_data(filepath='data-2897-2016-11-23.json'):
    with open(filepath, encoding='windows-1251') as f:
        return json.load(f)


def get_biggest_bar(data):
    return 'Самый большой бар (json):\n{}'.format(max(data, key=lambda x: x['SeatsCount']))


def get_smallest_bar(data):
    return 'Самый маленький бар (json):\n{}'.format(min(data, key=lambda x: x['SeatsCount']))


def get_closest_bar(data, longitude, latitude):
    def distance(lat_origin, lon_origin, lat_destination, lon_destination):
        """distance in meters between two (lat, lon) tuples"""

        radius = 6371009  # metres WGS-84 model

        dlat = math.radians(lat_destination - lat_origin)
        dlon = math.radians(lon_destination - lon_origin)
        a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat_origin)) \
                                                      * math.cos(math.radians(lat_destination)) * math.sin(
            dlon / 2) * math.sin(
            dlon / 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        d = radius * c
        return d

    return 'Самый близкий бар к {}, {} (json):\n{}'.format(longitude, latitude,
                                                       min(data, key=lambda x: distance(latitude, longitude,
                                                                                        float(x['Latitude_WGS84']),
                                                                                        float(x['Longitude_WGS84']))))

if __name__ == '__main__':
    data = load_data()
    splitter = '-'*50
    print(get_biggest_bar(data))
    print(splitter)
    print(get_smallest_bar(data))
    print(splitter)
    print('Поиск самого близкого бара.')
    lat_inp = float(input('Введите широту (например 55.701101): ').replace(',', '.'))
    lon_inp = float(input('Введите долготу (например 37.638228): ').replace(',', '.'))
    print(get_closest_bar(data, lon_inp, lat_inp))
