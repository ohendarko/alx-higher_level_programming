#!/usr/bin/python3
"""contains the class definition of a State and
an instance Base = declarative_base()"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class State(Base):
    """class name"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    db_url = "mysql://username:password@localhost:3306/your_database"
    engine = create_engine(db_url, echo=True)  # Set echo to True for debugging
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name='New State')
    session.add(new_state)
    session.commit()
    session.close()
