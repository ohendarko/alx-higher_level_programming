#!/usr/bin/python3
"""Write a script that lists all State objects
from the database hbtn_0e_6_usa"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states(username, password, database_name):
    db_url = f"mysql: //{username}: {password}@localhost: 3306/{database_name}"
    engine = create_engine(db_url, echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")
    session.close()


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage:")
        sys.exit(1)
    username, password, database_name = sys.argv[1:4]
    list_states(username, password, database_name)
