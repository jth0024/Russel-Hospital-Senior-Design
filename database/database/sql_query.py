from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sql_declarative import Base, devices, errors, maintenance, controllerone,controllertwo, setpoints

def row2dict(row):
        #Purpose: Purpose of method is to take a row of database values and creates a dictionary in which the name of the column, i.e. tempOA, is used as the key
	#if statement is used to skip over values that are written as None
    d = {}
    for column in row.__table__.columns:
    	if str(getattr(row, column.name)) != 'None':
        	d[column.name] = str(getattr(row, column.name))
    return d

def list2dict(list):

    #Purpose: Purpose of method is to take a list and create a dictionary from that list. 
	#The list is assumed to be a tuple and the key is the first item of the tuple
	d = {}
	for i in range(0, len(list)):
		key = list[i][0]
		d[key]= list[i]
	return d

def queryRow(tableName, path):
    	#Purpose: Purpose of code is to query the last inserted row of a table given the table name

	#switch cases are used so that the function that calls queryRow doesn't have to import the classes
	#found in sql_declarative. 
	######
	#NOTE: if a new device or data table is added it needs to be added here as well and imported on line three
	######
	if tableName == "devices":
		table = devices
	elif tableName == "base":
		table = base
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
	#the engine calls the dictionary called rh.db
	#sqlite:/// with three forward slashes allow you to choose a directory using an relative path
	#sqlite://// with four forward slashes allows you to choose a directory using an absolute path
	engine = create_engine(path)
	Base.metadata.bind = engine
	DBSession = sessionmaker()
	DBSession.bind = enginesession = DBSession()
	session = DBSession()
	#Functions assume that the desired output is the last value inputed into the database, arranged by auto-incrementing id
	#query is then converted into a dictionary in which the database's column name is the key and the value is value.
	databaseRow = session.query(table).order_by(table.id.desc()).first()
	dict = row2dict(databaseRow)
	return dict

def queryRowSpecific(tableName,key,columnName):
	#Purpose: To be able to query a specific row in the table, not just the last row.
	#Using the queryTable function to get a dictionary of the entire table with the key selected by the use i.e. name, ipaddress, timestamp, ect, ect... 
	#Function then returns a single row's dictionary in which the key needed to access the specified row 
	#needs to be the column name
	table = queryTable(tableName,key)
	value = table[columnName]
	return value

def queryColumn(tableName,columnName, path):
	#Purpose: Purpose of method is to query a specific column of the table
	#switch cases are used so that the function that calls queryColumn doesn't have to import the classes
	#found in sql_declarative. 
	######
	#NOTE: if a new device or data table is added it needs to be added here as well and import on line three
	######
	if tableName == "devices":
		table = devices
	elif tableName == "base":
		table = base
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
	#the engine calls the dictionary called rh.db
	#sqlite:/// with three forward slashes allow you to choose a directory using an relative path
	#sqlite://// with four forward slashes allows you to choose a directory using an absolute path
	#engine = create_engine('sqlite:///../database/database/rh.db')
	engine = create_engine(path)
	Base.metadata.bind = engine
	DBSession = sessionmaker()
	DBSession.bind = enginesession = DBSession()
	session = DBSession()
	list = []
	varableSelect = getattr(table,columnName)
	for value in session.query(varableSelect):
		 list.append(value[0])
	return list
	#appending line calls out the zeroth spot in a list to only place only the desired string into the list 


def queryTable(tableName, key, path):
    	#Purpose: Method takes the take name to query and returns a dictionary composed of a dictionary that contain all of the row information.
	#The dictionary that contains the row information uses the column name as the key, while the returned dictionary uses the unique ID as the key

	#Switch cases are used so that the function that calls queryTable doesn't have to import the classes
	#found in sql_declarative. 
	######
	#NOTE: if a new device or data table is added it needs to be added here as well and import on line three
	######
	if tableName == "devices":
		table = devices
	elif tableName == "base":
		table = base
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
	#the engine calls the dictionary called rh.db
	#sqlite:/// with three forward slashes allow you to choose a directory using an relative path
	#sqlite://// with four forward slashes allows you to choose a directory using an absolute path
	engine = create_engine(path)

	Base.metadata.bind = engine
	DBSession = sessionmaker()
	DBSession.bind = enginesession = DBSession()
	session = DBSession()
	dict = {}
	#Functions assume that the desired output is the last value inputed into the database, arragned by auto-incrementing id
	for row in session.query(table):
		innerDict = row2dict(row)
		dict[innerDict[key]]= innerDict
	return dict


def queryValue(tableName,columnName, path):
    	#Purpose: Method uses SQLalchemy to return a single value. The value is determined by the columnName and is found on the last row.
	#switch cases are used so that the function that calls insertNewRow doesn't have to import the classes
	#found in sql_declarative. 
	######
	#NOTE: if a new device or data table is added it needs to be added here as well and import on line three
	######
	if tableName == "devices":
		table = devices
	elif tableName == "base":
		table = base
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
	#the engine calls the dictionary called rh.db
	#sqlite:/// with three forward slashes allow you to choose a directory using an relative path
	#sqlite://// with four forward slashes allows you to choose a directory using an absolute path
	engine = create_engine(path)
	Base.metadata.bind = engine
	DBSession = sessionmaker()
	DBSession.bind = enginesession = DBSession()
	session = DBSession()
	varableSelect = getattr(table,columnName)
	value  = session.query(varableSelect).order_by(table.id.desc()).first()
	return value[0]

def queryValueSpecific(tableName,columnName,rowName,rowValue, path):
	#Purpose: Method uses SQLalchemy to return a single value. The value is determined by the columnName the row is 
	#determined where the given row value is found and the given row.

	#switch cases are used so that the function that calls insertNewRow doesn't have to import the classes
	#found in sql_declarative. 
	######
	#NOTE: if a new device or data table is added it needs to be added here as well and import on line three
	######
	if tableName == "devices":
		table = devices
	elif tableName == "base":
		table = base
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
		#the engine calls the dictionary called rh.db
	#sqlite:/// with three forward slashes allow you to choose a directory using an relative path
	#sqlite://// with four forward slashes allows you to choose a directory using an absolute path
	engine = create_engine(path)
	Base.metadata.bind = engine
	DBSession = sessionmaker()
	DBSession.bind = enginesession = DBSession()
	session = DBSession()
	varableSelect = getattr(table,columnName)
	indication = getattr(table,rowName)
	value  = session.query(varableSelect).filter(indication == rowValue)
	return value[0][0]
