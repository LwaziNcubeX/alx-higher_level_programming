#!/usr/bin/python3
"""
Lists all State objects that contain the letter a from the database
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


def list_states_with_a():
    """
    Lists all State objects that contain the letter a from the database
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id).all()

    for state in states:
        print('{}: {}'.format(state.id, state.name))
    session.close()


if __name__ == "__main__":
    list_states_with_a()
