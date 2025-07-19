#!/usr/bin/python3
"""
Creates the states table in the database using SQLAlchemy.
"""

import sys
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./6-model_state.py <mysql username> <mysql password> <database name>")
        sys.exit(1)

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)
