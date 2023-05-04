import requests
from settings import TOKEN


host = 'https://cloud-api.yandex.net/'

def get_headers():
    return {'Content-Type': 'application/json', 'Authorization': f'OAuth {TOKEN}'}

def create_folder(name_folder):
    uri = 'v1/disk/resources/'
    url = host + uri
    params = {'path': f'/{name_folder}'}
    response = requests.put(url, headers=get_headers(), params=params)
    return response.status_code


if __name__ == "__main__":
    create_folder('1')
