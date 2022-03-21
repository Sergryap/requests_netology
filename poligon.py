import requests
import os
import json


class YaUploader:
    URL = 'https://cloud-api.yandex.net/v1/disk/resources'

    def __init__(self, token):
        self.token = token
        self.headers = {'Content-Type': 'application/json', 'Accept': 'application/json',
                        'Authorization': f'OAuth {token}'}

    def __create_folder(self, path):
        """Создание папки на диске."""
        requests.put(f'{YaUploader.URL}?path={path}', headers=self.headers)

    def upload(self, file_path, ya_dir):
        """Метод загружает файлы из папки file_path в папку ya_dir на яндекс дискe"""
        self.__create_folder(ya_dir)
        file_list = os.listdir(file_path)
        for file in file_list:
            file_list_path = os.path.join(file_path, file)
            res = requests.get(f"{YaUploader.URL}/upload?path={ya_dir}/{file}&overwrite=true",
                               headers=self.headers)
            link = res.json()['href']
            with open(file_list_path, 'rb') as f:
                requests.put(link, files={'file': f})


if __name__ == '__main__':
    BASE_PATH = os.getcwd()
    FILE_DIR = "loadfiles"
    FILE_PATH = os.path.join(BASE_PATH, FILE_DIR)
    YA_DIR = 'test1'  # Дирректория для загрузки на я-диск
    TOKEN = ""

    uploader = YaUploader(TOKEN)
    uploader.upload(FILE_PATH, YA_DIR)
