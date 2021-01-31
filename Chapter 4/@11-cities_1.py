def cities(city, country):
    city = f"{city.title()}, {country.title()}"
    return city

city = cities('newyork', 'america')
print(city)