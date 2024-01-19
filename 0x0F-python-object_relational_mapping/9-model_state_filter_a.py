#!/usr/bin/python3
"""a script that lists all State objects that contain the letter a
from the database hbtn_0e_6_usa"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states_with_letter_a(username, password, database_name):
    db_url = f"mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}"
    engine = create_engine(db_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")
    session.close()


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage:")
        sys.exit(1)
    username, password, database_name = sys.argv[1:4]
    list_states_with_letter_a(username, password, database_name)
