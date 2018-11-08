#!/usr/bin/python3
from pprint import pprint as pp

country_to_capital = { 'UK': 'London',
                       'Brazil': 'Brazilia',
                       'Moracco': 'Rabat',
                       'Sweden': 'Stockholm'}

cap_to_country = {capital: country for country, capital in country_to_capital.items()}
pp(country_to_capital)
print()
pp(cap_to_country)


