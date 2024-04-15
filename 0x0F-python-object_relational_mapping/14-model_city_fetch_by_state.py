#!/usr/bin/python3
"""script that prints all City objects from the database hbtn_0e_14_usa"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(State.name, City.id, City.name).order_by(City.id)
    for city in cities.filter(State.id == City.state_id):
        print(city[0] + ": (" + str(city[1]) + ") " + city[2])
