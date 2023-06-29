#!/usr/bin/python3
"""script prints the State object with name
passed as argument from database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    import sys
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from model_state import Base, State

    if len(sys.argv) != 5:
        sys.exit(1)
    username = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    search_state = sys.argv[4]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{passwd}@localhost:3306/{db_name}"
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    state_query = session.query(State).filter(
        State.name == search_state
        ).first()
    if state_query:
        print(state_query.id)
    else:
        print("Not found")
    session.close()
