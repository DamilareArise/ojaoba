
import requests
from decouple import config

def getCountries():
    try:
        url = "https://country-state-city-search-rest-api.p.rapidapi.com/allcountries"

        headers = {
            "x-rapidapi-key": config("x-rapidapi-key"),
            "x-rapidapi-host": config("x-rapidapi-host")
        }

        response = requests.get(url, headers=headers)

        countries =[(country['isoCode'], country['name']) for country in response.json()]
        
        return countries
    except Exception as e:
        print(e)
        return [
            ('us', 'United States'),
            ('ca', 'Canada'),
            ('gb', 'United Kingdom'),
            ('au', 'Australia'),
            ('fr', 'France'),
            ('de', 'Germany'),
            ('jp', 'Japan'),
            ('cn', 'China'),
            ('in', 'India'),
            ('br', 'Brazil')
        ]


def getState(isoCode):
    try:
        url = "https://country-state-city-search-rest-api.p.rapidapi.com/states-by-countrycode"

        querystring = {"countrycode":isoCode}

        headers = {
            "x-rapidapi-key": config("x-rapidapi-key"),
            "x-rapidapi-host": config("x-rapidapi-host")
        }

        response = requests.get(url, headers=headers, params=querystring)
        
        states = [(state['name'].lower(), state['name'] )for state in response.json()]
        
        return states
    except Exception as e:
        print(e)
        return [
            ('california', 'California'),
            ('texas', 'Texas'),
            ('florida', 'Florida'),
            ('new york', 'New York'),
            ('illinois', 'Illinois'),
            ('pennsylvania', 'Pennsylvania'),
            ('ohio', 'Ohio'),
            ('georgia', 'Georgia'),
            ('north carolina', 'North Carolina'),
            ('michigan', 'Michigan')
        ]

# print(getCountries())

# print(getState('us'))