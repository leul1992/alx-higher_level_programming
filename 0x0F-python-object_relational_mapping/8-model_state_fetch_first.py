#!/usr/bin/python3
"""prints the first state object"""
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    session = Session(engine)

    state = session.query(State).order_by(State.id).first()
    if (state):
        print(f'{state.id}: {state.name}')
    else:
        print('/n')
    session.close()
