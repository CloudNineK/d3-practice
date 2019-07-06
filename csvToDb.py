import pandas as pd
import sqlite3
import re

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import create_engine


Base = declarative_base()

class Vehicle(Base):
    __tablename__ = 'Vehicle'

    urlID = Column(Integer, primary_key=True)
    url = Column(String())
    price = Column(Integer)
    city = Column(String())
    year = Column(Integer)
    color = Column(String())
    fuel = Column(String())
    cylinders = Column(String())
    desc = Column(String())
    lat = Column(Float())
    lon = Column(Float())

def appendUniqueID(data):
    matchID = re.compile(r'/\d+')
    def sliceID(s):
        cID = matchID.search(s)
        cID = int(cID.group()[1:])
        return cID

    data['ID'] = data['url'].apply(sliceID)
    data = data.drop_duplicates(subset='ID', keep='first')

if __name__ == '__main__':

    # Create db
    engine = create_engine('sqlite:///craigslistVehicles.db')
    Base.metadata.create_all(engine)

    # csv to dataframe; massage
    data = pd.read_csv('craigslistVehicles.csv')
    appendUniqueID(data)
    data = data.rename(index=str, columns={'paint_color': 'color'})
    data = data[
        ['url', 'city', 'price', 'year', 'manufacturer', 'make', 
         'condition', 'fuel', 'color', 'image_url', 'lat', 'long', 'ID' ]]
    data = data.dropna()


    # dump to db
    data.to_sql('Vehicle', con=engine, if_exists='replace', chunksize=2000)