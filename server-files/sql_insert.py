from sqlalchemy import create_engine, insert
from sqlalchemy.orm import sessionmaker
 
from sqlalchemy_declarative import Base, Devices
 
engine = create_engine('sqlite:///rh.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()
 
# Insert a Person in the person table
# new_device1 = Devices(name='device 1', ini='controller1', ip='192.168.92.65', mac='poop')
# new_device2 = Devices(name='device 2', ini='controller2', ip='192.168.92.67', mac='poop')
# session.add(new_device2,new_device1)
# session.commit()


table = 'devices'
input = {'name': 'device3', 'ini':'controller3','ip':'192.168.92.44', 'mac':'hello Im a mac'}

while input:
    values = dict((input.pop(0), input.pop(0)))
    obj = MyObject(**values)
    session.add(obj)
session.commit()
	