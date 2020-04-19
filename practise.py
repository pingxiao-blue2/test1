def get_formatted_city(country,city,contry= ''):
    if contry:
        full_place = country + ' ' + city + ' ' + contry
    else:
        full_place = country + ' ' + city
    return full_place.title()
cityname = get_formatted_city('cc','ss','gg')
cityname1 = get_formatted_city('ac','as')
print(cityname)
print(cityname1)
