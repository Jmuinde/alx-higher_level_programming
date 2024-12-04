#!/usr/bin/env python3
"""Start link class to the table in database
"""

import sys
import sqlalchemy as db
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = db.create_engine('mysql+mysqldb://{}:{}@localhost/{}?unix_socket=/var/run/mysqld/mysqld.sock'.format(sys.argv[1], sys.argv[2], sys.argv[3]     ), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(State).filter(State.name.like('%a%')).delete()
    session.commit()

    session.close()
