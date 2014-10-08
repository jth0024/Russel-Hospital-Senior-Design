import os

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///rh.db')
DBSession = sessionmaker(bind=engine)