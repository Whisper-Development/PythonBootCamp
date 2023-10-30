#Starting travel log 

travel_log = [
    {
        "country": "England",
        "visits" : 1,
        "cities" : ["London", "Sheffield", "Liverpool"]
    },
    {
        "country": "Ireland",
        "visits": 3,
        "cities" : ["Dublin"]
    }

]

country = input()
visits = int(input())
list_of_cities = eval(input())

def add_new_country(country, visits, list_of_cities):
    new_country = {
        "country": country,
        "visits" : visits,
        "cities" : list_of_cities
    }
    travel_log.append(new_country)

add_new_country(country, visits, list_of_cities)