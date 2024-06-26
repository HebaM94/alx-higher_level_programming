#!/usr/bin/python3
"""script that lists all City objects from
the database hbtn_0e_101_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    objs = session.query(State).join(State.cities).order_by(City.id)
    for obj in objs:
        for city in obj.cities:
            print("{}: {} -> {}".format(city.id, city.name, obj.name))
