import csv, json
from geojson import Feature, FeatureCollection, Point

features = []
with open('master_authors - Sheet1.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for book_id, latitude, longitude, weather, temp in reader:
        latitude, longitude = map(float, (latitude, longitude))
        features.append(
            Feature(
                geometry = Point((longitude, latitude)),
                properties = {
                    'weather': weather,
                    'temp': temp
                }
            )
        )

collection = FeatureCollection(features)
with open("GeoObs.json", "w") as f:
    f.write('%s' % collection)