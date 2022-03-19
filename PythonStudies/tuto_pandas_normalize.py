import pandas as pd
import json
import requests

print('Tutorial from '
      'https://towardsdatascience.com/all-pandas-json-normalize-you-should-know-for-flattening-json-13eae1dfb7dd'
      )
print('------------------------------ DF1 (Simple JSON) ------------------------------')
a_dict = {
    'school': 'ABC primary school',
    'location': 'London',
    'ranking': 2,
}
df = pd.json_normalize(a_dict)
print(df)

print('------------------------------ DF2 (JSON with multiple levels) ------------------------------')
json_list = [
    {'class': 'Year 1', 'student number': 20, 'room': 'Yellow'},
    {'class': 'Year 2', 'student number': 25, 'room': 'Blue'},
]
df2 = pd.json_normalize(json_list)
print(df2)

print('------------------------------ DF3 (keys that are not always present) ------------------------------')
json_list = [
    {'class': 'Year 1', 'num_of_students': 20, 'room': 'Yellow'},
    {'class': 'Year 2', 'room': 'Blue'},  # no num_of_students
]
df3 = pd.json_normalize(json_list)
print(df3)

print('------------------------------ DF4 (JSON with a nested list) ------------------------------')
json_obj = {
    'school': 'ABC primary school',
    'location': 'London',
    'ranking': 2,
    'info': {
        'president': 'John Kasich',
        'contacts': {
            'email': {
                'admission': 'admission@abc.com',
                'general': 'info@abc.com'
            },
            'tel': '123456789',
        }
    }
}
df4 = pd.json_normalize(json_obj)
print(df4)
print(df4.info())

print('------------------------------ DF5 (max_level Argument) ------------------------------')
df5 = pd.json_normalize(json_obj, max_level=1)
print(df5)

print('------------------------------ DF6 (list of dicts) ------------------------------')
json_list_of_dicts = [
    {
        'class': 'Year 1',
        'student count': 20,
        'room': 'Yellow',
        'info': {
            'teachers': {
                'math': 'Rick Scott',
                'physics': 'Elon Mask'
            }
        }
    },
    {
        'class': 'Year 2',
        'student count': 25,
        'room': 'Blue',
        'info': {
            'teachers': {
                'math': 'Alan Turing',
                'physics': 'Albert Einstein'
            }
        }
    },
]

df6 = pd.json_normalize(json_list_of_dicts)
print(df6)
print('------------------------------ DF6 (max_level argument) ------------------------------')
df6_ml1 = pd.json_normalize(json_list_of_dicts, max_level=1)
print(df6_ml1)

print('------------------------------ DF7 ------------------------------')
json_obj_with_nested_list = {
    'school': 'ABC primary school',
    'location': 'London',
    'ranking': 2,
    'info': {
        'president': 'John Kasich',
        'contacts': {
            'email': {
                'admission': 'admission@abc.com',
                'general': 'info@abc.com'
            },
            'tel': '123456789',
        }
    },
    'students': [
        {'name': 'Tom'},
        {'name': 'James'},
        {'name': 'Jacqueline'}
    ],
}

df7 = pd.json_normalize(json_obj_with_nested_list)
print(df7)
df7_rp1 = pd.json_normalize(json_obj_with_nested_list, record_path=['students'])
print('------------------------------ DF7 (record_path) ------------------------------')
print(df7_rp1)

print('------------------------------ DF7 (meta) ------------------------------')
df7_meta = pd.json_normalize(
    json_obj_with_nested_list,
    record_path=['students'],
    meta=['school', ['info', 'contacts', 'tel'], ['info', 'contacts', 'email', 'general']],
)
print(df7_meta)

print('------------------------------ DF8 ------------------------------')
json_list_data_list_of_dicts = [
    {
        'class': 'Year 1',
        'student count': 20,
        'room': 'Yellow',
        'info': {
            'teachers': {
                'math': 'Rick Scott',
                'physics': 'Elon Mask'
            }
        },
        'students': [
            {
                'name': 'Tom',
                'sex': 'M',
                'grades': {'math': 66, 'physics': 77}
            },
            {
                'name': 'James',
                'sex': 'M',
                'grades': {'math': 80, 'physics': 78}
            },
        ]
    },
    {
        'class': 'Year 2',
        'student count': 25,
        'room': 'Blue',
        'info': {
            'teachers': {
                'math': 'Alan Turing',
                'physics': 'Albert Einstein'
            }
        },
        'students': [
            {'name': 'Tony', 'sex': 'M'},
            {'name': 'Jacqueline', 'sex': 'F'},
        ]
    },
]

df8 = pd.json_normalize(json_list_data_list_of_dicts)
print(df8)
print('------------------------------ DF8 (record_path) ------------------------------')
df8_rp = pd.json_normalize(json_list_data_list_of_dicts, record_path='students')
print(df8_rp)
print('------------------------------ DF8 (meta) ------------------------------')
df8_meta = pd.json_normalize(
    json_list_data_list_of_dicts,
    record_path='students',
    meta=['class', 'room', ['info', 'teachers', 'math'], ['info', 'teachers', 'physics']]
)
print(df8_meta)

print('------------------------------ DF9 (errors) ------------------------------')
data_errors = [
    {
        'class': 'Year 1',
        'student count': 20,
        'room': 'Yellow',
        'info': {
            'teachers': {
                'math': 'Rick Scott',
                'physics': 'Elon Mask',
            }
        },
        'students': [
            {'name': 'Tom', 'sex': 'M'},
            {'name': 'James', 'sex': 'M'},
        ]
    },
    {
        'class': 'Year 2',
        'student count': 25,
        'room': 'Blue',
        'info': {
            'teachers': {
                # no math teacher
                'physics': 'Albert Einstein'
            }
        },
        'students': [
            {'name': 'Tony', 'sex': 'M'},
            {'name': 'Jacqueline', 'sex': 'F'},
        ]
    },
]

df9 = pd.json_normalize(data_errors, record_path='students', meta=['class', 'room', ['info', 'teachers', 'math']],
                        errors='ignore')
print(df9)

print('------------------------------ DF10 (sep) ------------------------------')
df10 = pd.json_normalize(
    data_errors,
    record_path='students',
    meta=['class', 'room', ['info', 'teachers', 'math']],
    errors='ignore',
    sep='->'
)
print(df10)

print('------------------------------ DF11 (meta & record_prefix) ------------------------------')
df11 = pd.json_normalize(
    data_errors,
    record_path='students',
    meta=['class'],
    record_prefix='student-',
    meta_prefix='meta-'
)
print(df11)

print('------------------------------ DF12 (local file) ------------------------------')

with open('data/json/Simple.json', 'r') as f:
    data_local_file = json.loads(f.read())

# Flattening JSON data
df12 = pd.json_normalize(data_local_file)
print(df12)

print('------------------------------ DF13 (url) ------------------------------')

URL = 'http://raw.githubusercontent.com/BindiChen/machine-learning/master/data-analysis/027-pandas-convert-json/data/simple.json'
data_url = json.loads(requests.get(URL).text)
df13 = pd.json_normalize(data_url)
print(df13)

