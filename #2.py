import requests
from pprint import pprint


class YaUploader:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_upload_link(self, path_to_file):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": path_to_file}
        response = requests.get(upload_url, headers=headers, params=params)
        # pprint(response.json())
        return response.json()

    def upload(self, path_to_file):
        href = self.get_upload_link(path_to_file=path_to_file).get("href", "")
        response = requests.put(href, data=open(path_to_file, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            return "Success"




if __name__ == '__main__':
    path_to_file = 'test.txt'
    token = 'AQAAAAAbMAVUAAgAJ2Omijv5GELyuFEx8BLrKd0'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file=path_to_file)
    print(result)
