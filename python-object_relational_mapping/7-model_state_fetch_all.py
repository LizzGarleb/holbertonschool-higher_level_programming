#!/usr/bin/python3
"""Lists all states object from the database"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    """Lists all state object from the database"""

    user = argv[1]
    password = argv[2]
    database = argv[3]

    engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@localhost/{database}")

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State).order_by(State.id)

    for state in results:
        print("{}: {}".format(states.id, states.name))
