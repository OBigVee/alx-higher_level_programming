#!/usr/bin/python3
"""
script list all State objects from the
database hbtn_0e_6_usa
"""

# if __name__ == "__main__":

#     import sys
#     from sqlalchemy import create_engine
#     from sqlalchemy.orm import sessionmaker
#     from sqlalchemy import URL

#     from model_state import State, Base

#     USERNAME = sys.argv[1]
#     PASSWORD = sys.argv[2]
#     DATABASE_NAME = sys.argv[3]
#     PORT = 3306

#     url_object = URL.create(
#         "mysql+mysqldb",
#         username="root",
#         password="thisme",
#         host="localhost",
#         database="hbtn_0e_6_usa",
#     )

#     engine = create_engine(url=url_object, pool_pre_ping=True)
#     Session = sessionmaker(bind=engine)
#     session = Session()

#     for row in session.query(State).all():
#         print(f"{row.id}: {row.name}")
#     session.close()
if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    _, user, passwd, db = sys.argv
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(user, passwd, db),
        pool_pre_ping=True,
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
