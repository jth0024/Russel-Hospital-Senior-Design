from sqlalchemy import create_engine, insert,update
from sqlalchemy.orm import sessionmaker
from sql_declarative import Base, devices, errors, maintenance, controllerone, controllertwo, setpoints
 
def insertNewRow(tableName, TheDict, path):
	#Purpose: Function takes the the table name(i.e. the class found in sql_declarative) and a dictionary to insert all of the values into the database

	#the engine calls the dictionary called rh.db
	#sqlite:/// with three forward slashes allow you to choose a directory using an relative path
	#sqlite://// with four forward slashes allows you to choose a directory using an absolute path
	engine = create_engine(path)
	#switch cases are used so that the function that calls insertNewRow doesn't have to import the classes
	#found in sql_declarative. 
	######
	#NOTE: if a new device or data table is added it needs to be added here as well and import on line three
	######
	
	if tableName == "devices":
		table = devices
	elif tableName == "errors":
		table = errors
	elif tableName == "maintenance":
		table = maintenance
	elif tableName == "controllerone":
		table = controllerone
	elif tableName == "controllertwo":
		table = controllertwo
	elif tableName == "setpoints":
		table = setpoints
	# Bind the engine to the metadata of the Base class so that the
	# declaratives can be accessed through a DBSession instance
	Base.metadata.bind = engine
	DBSession = sessionmaker(bind=engine)
	session = DBSession()
	l = insert(table)
	l = l.values(TheDict)
	session.execute(l)
	session.commit()


	####SQLalchemy note####
	# A DBSession() instance establishes all conversations with the database
	# and represents a "staging zone" for all the objects loaded into the
	# database session object. Any change made against the objects in the
	# session won't be persisted into the database until you call
	# session.commit(). If you're not happy about the changes, you can
	# revert all of them back to the last commit by calling
	# session.rollback()
