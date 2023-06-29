#!/usr/bin/python3
"""script adds state object "Louisiana" to DB
"""

if __name__ == "__main__":
    import sys
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from model_state import Base, State

    _, username, passwd, db = sys.argv
    engine = create_engine(
        f"mysql+mysqldb://{username}:{passwd}@localhost:3306/{db}"
        )
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")

    session.add(new_state)
    session.commit()

    print(new_state.id)

    session.close()
