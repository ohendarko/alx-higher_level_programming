#!/usr/bin/python3
"""script that deletes all State objects with a name containing the letter
'a' from the database hbtn_0e_6_usa using SQLAlchemy:"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def delete_states_with_letter_a(username, password, database_name):
    db_url = f"mysql://{username}:{password}@localhost:3306/{database_name}"
    engine = create_engine(db_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states_to_delete = session.query(State).filter(
        State.name.like('%a%')).all()

    for state in states_to_delete:
        session.delete(state)

    session.commit()
    print(f"{len(states_to_delete)} state(s) deleted successfully")
    session.close()


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage:")
        sys.exit(1)
    username, password, database_name = sys.argv[1:4]
    delete_states_with_letter_a(username, password, database_name)
