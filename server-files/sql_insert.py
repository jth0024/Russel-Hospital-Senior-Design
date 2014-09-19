from sqlalchemy import create_engine, insert,update
from sqlalchemy.orm import sessionmaker
from sql_query import queryRow
 
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


# populate = ['device3','controller3','192.168.92.44','hello Im a mac']
# #{'ini': 'controller2', 'ip': '192.168.92.67', 'mac': 'poop', 'id': '1', 'name': 'device 2'}

# i = insert(table)
# i = i.values({'name': 'device 3','ini': 'controller3', 'ip': '192.168.92.67', 'mac': 'poop'})
# session.execute(i)
# session.commit()

def insertNewRow(table, dictKeys,*args):
	l = insert(table)
	TheDict = {}
	keytupletemp = tuple(dictKeys)
	for i in range(0,len(args)):
		print i
		keytuple = keytupletemp[i]
		value = args[i]
		TheDict[keytuple] = value
		print TheDict
	session.execute(l)
	session.commit()

table = Devices
deviceDict = queryRow(table)
print deviceDict
insertNewRow(table,deviceDict.keys(),'deviceJosh','controllerJosh','192.168.92.Josh','hello Im a Josh')
results = queryRow(table)
print results



	# def userInput(ItemA, ItemB, *args):    
 #    lst=[]
 #    lst.append(ItemA)
 #    lst.append(ItemB)
 #    for arg in args:
 #        lst.append(arg)

 #    print ' '.join(lst)