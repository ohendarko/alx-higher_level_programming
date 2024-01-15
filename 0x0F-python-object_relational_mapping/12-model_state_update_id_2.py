#!/usr/bin/python3
"""a script that changes the name of a State object
from the database hbtn_0e_6_usa using SQLAlchemy"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def change_state_name(username, password, database_name):
    db_url = f"mysql: //{username}: {password}@localhost: 3306/{database_name}"
    engine = create_engine(db_url, echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_to_update = session.query(State).filter_by(id=2).first()

    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()
        print("Name updated successfully")
    else:
        print("State with id=2 not found")
    session.close()


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage:")
        sys.exit(1)
    username, password, database_name = sys.argv[1:4]
    change_state_name(username, password, database_name)
