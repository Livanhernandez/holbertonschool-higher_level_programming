#!/usr/bin/python3
"""create new state"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == '__main__':
    user = argv[1]
    password = argv[2]
    db = argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{user}:{password}@localhost:3306/{db}'
    )

    session = sessionmaker(bind=engine)
    session = session()

    new_state = State(name='Lousiana')

    session.add(new_state)
    session.commit()

    states = session.query(State).filter(State.name == "Lousiana").all()
    [print(f"{state.id}") for state in states]

    session.close()
