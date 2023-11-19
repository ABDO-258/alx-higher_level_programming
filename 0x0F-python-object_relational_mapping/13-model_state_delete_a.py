#!/usr/bin/python3
"""Start link class to table in database """
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    letter = 'a'

    states_delete = session.query(State).filter(State.name.ilike('%a%')).all()
    if states_delete:
        for st in states_delete:
            session.delete(st)
        session.commit()
    session.close()
