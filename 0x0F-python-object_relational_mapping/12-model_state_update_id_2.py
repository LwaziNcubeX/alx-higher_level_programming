#!/usr/bin/python3
"""
Changes the name of a State object from the database
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


def change_state_name():
    """
    Changes the name of a State object from the database
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

    state = session.query(State).filter(State.id == 2).first()

    if state is not None:
        state.name = "New Mexico"
        session.commit()

    session.close()


if __name__ == "__main__":
    change_state_name()
