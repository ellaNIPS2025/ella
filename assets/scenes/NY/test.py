import json

place_metadata = json.load(open('place_metadata.json'))
building_metadata = json.load(open('building_metadata.json'))

places_in_place_metadata = []
places_in_building_metadata = []

for place in place_metadata:
    places_in_place_metadata.append(place)

for building in building_metadata:
    for place in building_metadata[building]["places"]:
        places_in_building_metadata.append(place["name"])

print(len(building_metadata.keys()))

print(len(places_in_place_metadata))
print(len(places_in_building_metadata))