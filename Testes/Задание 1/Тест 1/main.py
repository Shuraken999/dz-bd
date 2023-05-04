def geo_city(geo_list):
    city_country = []
    print('Визиты из Российских городов:')
    for visit in geo_list:
      for city, country in visit.values():
        if country =='Россия':
            city_country.append(city)
    result = city_country
    return result


if __name__ == "__main__":
    geo_logs = [
        {'visit1': ['Москва', 'Россия']},
        {'visit2': ['Дели', 'Индия']},
        {'visit3': ['Владимир', 'Россия']},
        {'visit4': ['Лиссабон', 'Португалия']},
        {'visit5': ['Париж', 'Франция']},
        {'visit6': ['Лиссабон', 'Португалия']},
        {'visit7': ['Тула', 'Россия']},
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit10': ['Архангельск', 'Россия']},
        {'visit11': ['Жигулёвск', 'Россия']}
    ]
    all_cities = geo_city(geo_logs)
    [print(i) for i in all_cities]
    # print(all_cities)
