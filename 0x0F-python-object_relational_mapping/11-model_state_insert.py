#!/usr/bin/python3i
"""
a script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy.sql import text


def search_state_by_name(username, password, database_name, state_name):
    db_url = f"mysql://{username}:{password}@localhost:3306/{database_name}"
    engine = create_engine(db_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = text("SELECT * FROM states WHERE name = :state_name")
    result = session.execute(query, {"state_name": state_name}).fetchone()

    if result:
        print(result.id)
    else:
        print("Not found")
    session.close()


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 5:
        print("Usage: ")
        sys.exit(1)
    username, password, database_name, state_name = sys.argv[1:5]
    search_state_by_name(username, password, database_name, state_name)
