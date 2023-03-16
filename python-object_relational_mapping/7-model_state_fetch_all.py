#!/usr/bin/python3
"""
Lists all states object from the database
"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    url = "mysql+mysqlconnector://{user}:{password}@localhost:3306/{database}"
    engine = create_engine(url.format(
        user=argv[1]
        password=argv[2]
        database=argv[3]
    ))

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(states.id).all()

    for state in states:
        print("{}: {}" states.id, states.name)
