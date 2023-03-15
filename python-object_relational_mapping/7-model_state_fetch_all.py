#!/usr/bin/python3
"""Lists all states object from the database"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    username = argv[1]
    psw = argv[2]
    db_name = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(username, psw, db_name), pool_pre_ping=True)

    session = sessionmaker(bind=engine)
    session = session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

