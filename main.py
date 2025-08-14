# Looping through maps
myMap = {"alice": 90, "bob": 70}

for key in myMap:
    print(key, myMap[key])

for val in myMap.values():
    print(val)

for key, val in myMap.items():
    print(key, val)