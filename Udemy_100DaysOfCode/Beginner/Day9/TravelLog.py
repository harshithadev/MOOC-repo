travel_log = [
    {
       "country" : "France",
       "visits" : 12,
       "cities" : ["Paris", "Dijon", "Lille"] 
    },
    {
        "country" : "India",
        "visits" : 19,
        "cities" : ["Chennai", "Mumabi", "Delhi","Kolkota","Banglore"] 
    },
]
def add_new_country(country, visits, cities):
    travel_log.append({"country":country, "visits":visits, "cities":cities})

add_new_country("Russia", 1, ["Moscow", "St Petersberg" ])

print(travel_log)