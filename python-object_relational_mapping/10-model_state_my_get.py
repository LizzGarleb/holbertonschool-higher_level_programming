#!/usr/bin/python3
"""Print the State object with the name passed"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    """Print the State object with the name passed """

    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    name = sys.argv[4]

    engine = create_engine(
        f"mysql+mysqldb://{user}:{password}@localhost:3306/{database}"
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter_by(name=name)
    if states:
        for state in states:
            print(f"{state.id}")
    else:
        print("Not found")