#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import Base, City
from model_state import State


def fetch_cities_by_state(username, password, database_name):
    db_url = f"mysql://{username}:{password}@localhost:3306/{database_name}"
    engine = create_engine(db_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        state_name = session.query(State).filter_by(
            id=city.state_id).first().name
        print(f"{state_name}: ({city.id}) {city.name}")
    session.close()


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage:")
        sys.exit(1)
    username, password, database_name = sys.argv[1:4]
    fetch_cities_by_state(username, password, database_name)
