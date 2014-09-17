from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from sqlalchemy_declarative import Base, Devices
 
engine = create_engine('sqlite:///rh.db')


Base.metadata.bind = engine

DBSession = sessionmaker()
DBSession.bind = enginesession = DBSession()
session = DBSession()

def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))
    return d

device1 = session.query(Devices).order_by(Devices.id.desc()).first()
dict = row2dict(device1)
print dict

