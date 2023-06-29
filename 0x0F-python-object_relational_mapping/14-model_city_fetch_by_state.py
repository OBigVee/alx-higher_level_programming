#!/usr/bin/python3
"""
script prints all city objects from the
database hbtn_0e_14_usa
"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from model_city import City
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine, asc

    _, username, passwd, db = sys.argv
    url = f"mysql+mysqldb://{username}:{passwd}@localhost:3306/{db}"
    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(asc(City.id)).all()
    for city in cities:
        print(f"{city.state.name}: ({city.id}) {city.name}")
    session.close()
