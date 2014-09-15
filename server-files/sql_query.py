from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from sqlalchemy_declarative import Base, Devices
 
engine = create_engine('sqlite:///rh.db')


Base.metadata.bind = engine

DBSession = sessionmaker()
DBSession.bind = enginesession = DBSession()
session = DBSession()

device1 = session.query(Devices).first()
print device1.id