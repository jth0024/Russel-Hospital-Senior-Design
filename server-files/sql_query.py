from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sqlite3
from sql_declarative import Base, Devices
 

def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))
    return d

def newrow2dict(row):
	d = {}
	for column in row.__table__.columns:
		d[column.name] = str(getattr(row, column.name))
		return d

def list2dict(list):
	d = {}
	for i in range(0, len(list)):
		key = list[i][0]
		d[key]= list[i]
	return d

def queryRow(tableName):
	#SQL alchemy process for creating the engine and session to query the database
	#insert table name as a variable not a string
	engine = create_engine('sqlite:///rh.db')
	Base.metadata.bind = engine
	DBSession = sessionmaker()
	DBSession.bind = enginesession = DBSession()
	session = DBSession()
	#Functions assume that the desired output is the last value inputed into the database, arragned by auto-incrementing id
	databaseRow = session.query(tableName).order_by(tableName.id.desc()).first()
	#return databaseRow
	#query is then converted into a dictionary in which the database's column name is the key and the value is value.
	dict = row2dict(databaseRow)
	return dict

def queryRowSpecific(tableName,rowName,rowValue):
	####Not Functioning####
	engine = create_engine('sqlite:///rh.db')
	Base.metadata.bind = engine
	DBSession = sessionmaker()
	DBSession.bind = enginesession = DBSession()
	session = DBSession()
	indication = getattr(tableName,rowName)
	databaseRow = session.query(tableName).filter(indication == rowValue).all()
	#return databaseRow[0]
	dict = row2dict(databaseRow)
	return dict
	#query is then converted into a dictionary in which the database's column name is the key and the value is value.
	#dict = row2dict(databaseRow)
	#return dict

def queryColumn(tableName,columnName):
	#SQL alchemy process for creating the engine and session to query the database
	#insert table name as a variable not a string, while the column name must be entered in as a string
	#column name is then converted from a string using the get attribute command
	engine = create_engine('sqlite:///rh.db')
	Base.metadata.bind = engine
	DBSession = sessionmaker()
	DBSession.bind = enginesession = DBSession()
	session = DBSession()
	list = []
	varableSelect = getattr(tableName,columnName)
	for value in session.query(varableSelect):
		 list.append(value[0])
	return list
	#appending line calls out the zeroth spot in a list to only place only the desired string into the list 


def queryTable(tableName):
	#Method takes the take name to query and returns a dictionary composed of a dictionary that contain all of the row information.
	#The dicitionary that contains the row information uses the column name as the key, while the returned dictionary uses
	#the unique ID as the key
	engine = create_engine('sqlite:///rh.db')
	Base.metadata.bind = engine
	DBSession = sessionmaker()
	DBSession.bind = enginesession = DBSession()
	session = DBSession()
	dict = {}
	#Functions assume that the desired output is the last value inputed into the database, arragned by auto-incrementing id
	for row in session.query(tableName):
		innerDict = row2dict(row)
		dict[innerDict['name']]= innerDict
	return dict


def queryValue(tableName,columnName):
	#Method uses SQLalchemy to return a single value. The value is determined by the columnName and is found on the last row.
	engine = create_engine('sqlite:///rh.db')
	Base.metadata.bind = engine
	DBSession = sessionmaker()
	DBSession.bind = enginesession = DBSession()
	session = DBSession()
	varableSelect = getattr(tableName,columnName)
	value  = session.query(varableSelect).order_by(tableName.id.desc()).first()
	return value[0]

def queryValueSpecific(tableName,columnName,rowName,rowValue):
	#Method uses SQLalchemy to return a single value. The value is determined by the columnName the row is 
	#determined where the given row value is found and the given row.
	engine = create_engine('sqlite:///rh.db')
	Base.metadata.bind = engine
	DBSession = sessionmaker()
	DBSession.bind = enginesession = DBSession()
	session = DBSession()
	varableSelect = getattr(tableName,columnName)
	indication = getattr(tableName,rowName)
	value  = session.query(varableSelect).filter(indication == rowValue)
	return value[0][0]


