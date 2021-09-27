import requests

from core.settings import API_GUANE_URL 


def upload_file(file: any):
    url = API_GUANE_URL
    filename = file.filename
    files = {'file': ('foobar.txt', open('file.txt','rb'), 'text/x-spam')}
    print(file)
    values = {'DB': 'photcat', 'OUT': 'csv', 'SHORT': 'short'}
    print(files)
    r = requests.post(url, files=files, data=values)
    print(r)
    return r.status_code