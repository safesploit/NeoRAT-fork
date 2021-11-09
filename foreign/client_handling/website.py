import webbrowser


def website(websites):
  for website in websites:
    if 'http://' not in website or 'https://' not in website:
      website = 'https://' + website
    webbrowser.open(website, new=2)
  
  return {'message': f'Websites succesfully opened', 'text_mode': 'success'}