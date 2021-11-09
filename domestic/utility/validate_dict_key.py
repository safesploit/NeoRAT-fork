def validate_dict_key(dictionary, key, lower=True):
  try:
    if lower:
      return dictionary[key].lower()
    else:
      return dictionary[key]      
  except KeyError:
    return None
  except:
    return dictionary[key]