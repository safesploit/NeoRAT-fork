import requests


def location_data():
  try:
    location = requests.get('http://ipinfo.io').json()
  except:
    return {'address': '???', 'location': '???'}
  else:
    try:
      return {'address': location['ip'], 'location': f'{location["city"]} ({location["country"]})'}
    except:
      try:
        return {'address': location['ip'], 'location': '???'}
      except:
        return {'address': '???', 'location': '???'}