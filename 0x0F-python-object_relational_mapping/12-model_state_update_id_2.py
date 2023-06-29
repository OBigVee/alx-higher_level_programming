#!/usr/bin/python3
"""script changes the name of a State object from
database hbtn_0e_6_usa
"""
if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    _, username, passwd, db = sys.argv
    engine = create_engine(
        f"mysql+mysqldb://{username}:{passwd}@localhost:3306/{db}"
        )
    Session = sessionmaker(bind=engine)
    session = Session()

    get_state = session.query(State).filter_by(id=2).first()

    if get_state:
        get_state.name = "New Mexico"

        session.commit()
    else:
        print("State not found")
    session.close()
