#!/usr/bin/python3
"""script deletes all State object with a name containing
the letter a from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    import sys
    from model_state import State, Base
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine

    _, username, passwd, db = sys.argv
    engine = create_engine(
        f"mysql+mysqldb://{username}:{passwd}@localhost:3306/{db}"
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    del_state = session.query(State).filter(State.name.like("%a%")).all()

    if del_state:
        for state in del_state:
            session.delete(state)
        session.commit()
        print("States deleted successfully")
    else:
        print("No states found with names containing 'a'.")
    session.close()
