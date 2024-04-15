#!/usr/bin/python3
"""script that creates the State “California” with
the City “San Francisco” from the database hbtn_0e_100_usa"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    st = State(name='California')
    city = City(name='San Francisco')
    st.cities.append(city)

    session.add(st)
    session.add(city)
    session.commit()
