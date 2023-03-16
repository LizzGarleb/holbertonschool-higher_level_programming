#!/usr/bin/python3
"""Lists first states object from the database"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    """Lists first state object from the database"""

    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{user}:{password}@localhost:3306/{database}"
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).order_by(State.id).first()
    for states in result:
        if result:
            print(f"{states.id}: {states.name}")
        else:
            print("Nothing")

    session.close()
