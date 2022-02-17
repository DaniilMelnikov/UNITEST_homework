import requests

import time

from pprint import pprint

class YandexDisk:
    def __init__(self, token_ya):
        self.token = token_ya
        self.headers = {
                'Content-Type': 'application/json',
                'Authorization': f'OAuth {self.token}'
            }

    def create_folder(self, name_folder):
        global new_folder
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        new_folder = name_folder
        params = {
            'path': name_folder
        }
        res = requests.put(url, params=params, headers=self.headers)
        counter = 0
        while True:
            counter += 1
            if res.status_code == 409:
                path = name_folder + '_' + str(counter)
                params = {
                    'path': path
                }
                res = requests.put(url, params=params, headers=self.headers)
            else:
                break
        return res.status_code

if __name__ == '__main__':
    folder_name = 'backup'
    token_ya = input('Токен из полигона: ')
    YaPeople = YandexDisk(token_ya)
    YaPeople.create_folder(folder_name)