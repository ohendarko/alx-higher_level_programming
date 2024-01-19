#!/usr/bin/python3
"""script that prints the first State object
from the database hbtn_0e_6_usa"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def fetch_first_state(username, password, database_name):
    db_url = (f"mysql+mysqldb://{username}:{password}@localhost:3306/"
              f"{database_name}")
    engine = create_engine(db_url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    first_state = session.query(State).order_by(State.id).first()

    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")
    session.close()


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: ")
        sys.exit(1)
    username, password, database_name = sys.argv[1:4]
    fetch_first_state(username, password, database_name)
