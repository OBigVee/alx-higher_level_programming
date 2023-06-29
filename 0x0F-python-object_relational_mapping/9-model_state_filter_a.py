#!/usr/bin/python3

# if __name__ == "__main__":
#     import sys
#     from sqlalchemy.orm import sessionmaker
#     from sqlalchemy import create_engine
#     from model_state import State, Base
    
#     username = sys.argv[1]
#     password = sys.argv[2]
#     DB = sys.argv[3]

#     engine = create_engine(
#         f"mysql+mysqldb://{username}:{password}@localhost:3306/{DB}"
#     )

#     #Base.metadata.bind = engine

#     Session = sessionmaker(bind=engine)
#     session = Session()

#     # states_a = session.query(State).filter(State.name.like("%a%")).order_by(
#     #     State.id.asc()).all()

#     #if states_a:
#     for state in session.query(State).filter(State.name.like("%a%")):
#         print(f"{state.id}: {state.name}")
#     # else:
#     #     print("Nothing")
#     # session.close()
#!/usr/bin/python3
"""Lists all State objects that contain the letter a
from the database hbtn_0e_6_usa"""


if __name__ == '__main__':
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    _, user, passwd, db = sys.argv
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(user,
                           passwd, db))
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).filter(State.name.like('%a%')):
        print('{}: {}'.format(state.id, state.name))