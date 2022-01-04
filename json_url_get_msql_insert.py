import requests
import pandas as pd
from sqlalchemy import create_engine
from requests.exceptions import HTTPError

# Data Source
url = 'https://reqres.in/api/products'
# Credentials to database connection (** REQUIRED TO RUN **)
hostname = "localhost"
dbname = "data_collect_html"
uname = "my_username"  # MySQL username
pwd = "my_password"  # MySQL password

# Create SQLAlchemy engine to connect to MySQL Database
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
                       .format(host=hostname, db=dbname, user=uname, pw=pwd))

try:
    r = requests.get(url)  # getting data
    # print(r.status_code)  # testing connection
    print(r.raise_for_status())
    jsonResponse = r.json()
    print('\n Entire JSON response:')
    print(jsonResponse)

    print('\n Print each key-value pair from JSON response:')
    for key, value in jsonResponse.items():
        print(key, ': ', value)

    print("\n Access directly using a JSON key name")
    print("Data is:")
    print(jsonResponse["data"])

    print('\n access nested JSON keys:')
    print('color is')
    print(jsonResponse["data"][0]["color"])

    # Create dataframe
    df = pd.json_normalize(jsonResponse['data'])
    # Convert dataframe to sql table
    df.to_sql('first_try', engine, index=False)
    cursor = engine.execute()

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')

