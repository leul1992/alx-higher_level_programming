#!/usr/bin/python3
"""lists all state objects from database hbtn_0e_6_usa"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    session = Session()
    for state in session.query(State).order_by(state.id).all():
        print('{}: {}'.format(state.id, state.name))
    session.close()
