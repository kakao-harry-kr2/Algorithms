import requests
import json

def clean_obj(obj, ret):
  for key, value in obj.items():
    if type(value) is dict:
      ret[key] = {}
      clean_obj(value, ret[key])
    
    elif type(value) is list:
      ret[key] = []
      for val in value:
        if val not in ['N/A', '-', '']:
          ret[key].append(val)
    
    elif value not in ['N/A', '-', '']:
      ret[key] = value

def clean_data():
  r = requests.get('https://coderbyte.com/api/challenges/json/json-cleaning')
  obj, ret = r.json(), {}

  clean_obj(obj, ret)

  return json.dumps(ret).replace(' ', '')

print(clean_data())