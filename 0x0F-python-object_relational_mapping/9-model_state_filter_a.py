#!/usr/bin/python3
"""Lists all State objects that contain the letter a
from the database hbtn_0e_6_usa
"""


if __name__ == "__main__":
    import sys
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from model_state import State, Base

    # username = sys.argv[1]
    # password = sys.argv[2]
    # DB = sys.argv[3]
    _, username, password, DB = sys.argv
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{DB}"
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).filter(State.name.like('%a%')):
        print(f"{state.id}: {state.name}")
