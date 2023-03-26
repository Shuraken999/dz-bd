import requests
import json
import re

from bs4 import BeautifulSoup
from fake_headers import Headers

HOST = "https://spb.hh.ru"
HHRU = f"{HOST}/search/vacancy?area=1&area=2&search_field=description&search_field=company_name&enable_snippets=true&text=python&text=django&text=flask"


def get_headers():
    return Headers(browser="firefox", os="win").generate()


def get_text(url):
    return requests.get(url, headers=get_headers()).text


def parse_article(vacancy):
    if vacancy is None:
        return
    name_company_city = vacancy.find(class_='vacancy-serp-item__info').text
    name_company = vacancy.find(class_='vacancy-serp-item__info').find('div').text
    pattern = r"((от)\s)*\d{1,5}\s(\d{1,3}\s)*(.{1,2}\s)*(\d{1,5}\s(\d{1,3}\s)*\w{3})+( на руки)*"
    info_vacancy = vacancy.find(class_='vacancy-serp-item-body').text
    salary = re.search(pattern, info_vacancy)
    if salary is None:
        sar = 'Доход не указан'
    else:
        sar = str(salary.group())
    return {
        "vacancy": vacancy.find(class_='serp-item__title').text,
        "link": vacancy.find(class_='serp-item__title')['href'],
        "salary": sar,
        "name_company": name_company,
        "name_city": name_company_city[len(name_company):],
    }


# вывод 5 страниц
page_all = {'', '&page=1', '&page=2', '&page=3', '&page=4'}
for end_page in page_all:
    main_page = get_text(f'{HHRU}{end_page}')
    bs = BeautifulSoup(main_page, features='lxml')
    counter = -1
    data_vacancy = []
    for job in bs.find_all(class_='serp-item'):
        data_vacancy.append(parse_article(job))
    for see in data_vacancy:
        print('vacancy: ' + see['vacancy'])
        print('link: ' + see['link'])
        print('salary: ' + see['salary'])
        print('name_company: ' + see['name_company'])
        print('name_city: ' + see['name_city'])
        print('')
with open('data.json', 'w') as f:
    json.dump(data_vacancy, f)
