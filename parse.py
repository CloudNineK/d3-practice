import pandas as pd
import re

def appendUniqueID(data):

    matchID = re.compile(r'/\d+')
    def sliceID(s):
        cID = matchID.search(s)
        cID = int(cID.group()[1:])
        return cID

    data['ID'] = data['url'].apply(sliceID)
    data = data.drop_duplicates(subset='ID', keep='first')

def ensureConventions(data):
    print(set(data['drive']))
    print(set(data['transmission']))
    print(set(data['fuel']))
    print(set(data['cylinders']))


if __name__ == "__main__":
    data = pd.read_csv('craigslistVehicles.csv')

    # Append unique ID based on url, remove duplicates
    appendUniqueID(data)
    # Rename color column
    data.rename({'paint_color': 'color'}, axis=1)
    print(data.columns)

    data = data[
        ['url', 'city', 'price', 'year', 'manufacturer', 'make', 
         'condition', 'fuel', 'paint_color', 'image_url', 'lat', 'long', 'id' ]
         ]
