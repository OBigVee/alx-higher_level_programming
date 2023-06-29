#!/usr/bin/python3

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import State, Base

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    DB = sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{DB}"
    )

    #Base.metadata.bind = engine

    Session = sessionmaker(bind=engine)
    session = Session()

    states_a = session.query(State).filter(State.name.like("%a%")).order_by(
        State.id.asc()).all()

    #if states_a:
    for state in states_a:
        print(f"{state.id}: {state.name}")
    # else:
    #     print("Nothing")
    # session.close()
