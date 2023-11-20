#!/usr/bin/python3
"""
Prints all City objects from the database
"""

import sys
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def fetch_cities():
    """
    Prints all City objects from the database
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        state_name = session.query(State).filter_by(
            id=city.state_id).first().name
        print("{}: ({}) {}".format(state_name, city.id, city.name))

    session.close()


if __name__ == "__main__":
    fetch_cities()
