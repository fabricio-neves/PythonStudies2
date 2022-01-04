import requests
from requests.exceptions import HTTPError
import pandas as pd

# r = requests.get('https://reqres.in/api/products')

# print(r.status_code)

# print(r.headers)

# print(r.headers['content-type'])

# print(r.text)

# receive = requests.get('https://imgs.xkcd.com/comics/making_progress.png')

# with open('data/img/image2.png', 'wb') as f:
#    f.write(receive.content)

# ploads = {'things': 2, 'total': 25}
# r = requests.get('https://httpbin.org/get', params=ploads)
# print(r.text)
# print(r.url)

# pload = {'username':'Olivia','password':'123'}
# r = requests.post('https://httpbin.org/post',data = pload)
# r_dictionary = r.json()
# print(r_dictionary['form'])

try:
    r = requests.get('https://reqres.in/api/products')
#    print(r.status_code)
#    print(r.raise_for_status())
    jsonResponse = r.json()
    print('\n Entire JSON response:')
    print(jsonResponse)
    print('\n Print each key-value pair from JSON response:')
    for key, value in jsonResponse.items():
        print(key, ': ', value)

    print("\n Access directly using a JSON key name")
    print("Data is ")
    print(jsonResponse["data"])

    print('\n access nested JSON keys:')
    print('color is')
    print(jsonResponse["data"][0]["color"])

    df = pd.json_normalize(jsonResponse)
    print('\n', df.info)

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
