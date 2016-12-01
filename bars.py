import json
import math


def load_data(filepath='bars.json'):
    with open(filepath, encoding='windows-1251') as f:
        return json.load(f)


def get_biggest_bar(bars_json):
    biggest_bar = max(bars_json, key=lambda x: x['SeatsCount'])
    return 'Самый большой бар: {}, кол-во мест: {} ({}).'.format(biggest_bar['Name'], biggest_bar['SeatsCount'],
                                                                 biggest_bar['Address'])


def get_smallest_bar(bars_json):
    smallest_bar = min(bars_json, key=lambda x: x['SeatsCount'])
    return 'Самый маленький бар: {}, кол-во мест: {} ({}).'.format(smallest_bar['Name'], smallest_bar['SeatsCount'],
                                                                   smallest_bar['Address'])


def distance_between_points(lat_origin, lon_origin, lat_destination, lon_destination):
    """distance in meters between two xx.xxxxx, yy.yyyyy points"""

    radius = 6371009  # metres WGS-84 model

    dlat = math.radians(lat_destination - lat_origin)
    dlon = math.radians(lon_destination - lon_origin)
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat_origin)) * math.cos(
        math.radians(lat_destination)) * math.sin(dlon / 2) * math.sin(dlon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = radius * c
    return distance


def get_closest_bar(data, longitude, latitude):
    closest_bar = min(data, key=lambda x: distance_between_points(latitude, longitude, float(x['Latitude_WGS84']),
                                                                  float(x['Longitude_WGS84'])))

    return 'Самый близкий бар к координатам ({}, {}): {}, кол-во мест: {} ({}).' \
           ''.format(latitude, longitude, closest_bar['Name'], closest_bar['SeatsCount'], closest_bar['Address'])


if __name__ == '__main__':
    bars_json = load_data()
    splitter = '-' * 50
    print(get_biggest_bar(bars_json))
    print(splitter)
    print(get_smallest_bar(bars_json))
    print(splitter)
    print('Поиск самого близкого бара.')
    while 1:
        try:
            lat_inp = float(input('Введите широту (например 55.701101): ').replace(',', '.'))
            lon_inp = float(input('Введите долготу (например 37.638228): ').replace(',', '.'))
            print(get_closest_bar(bars_json, lon_inp, lat_inp))
            break
        except ValueError:
            print('Неверный формат. Попробуйте еще раз.')
