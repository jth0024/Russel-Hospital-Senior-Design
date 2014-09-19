from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from sqlalchemy_declarative import Base, Devices
 
def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))
    return d

def queryRow(tableName):
	#SQL alchemy procesc for creating the engine and session to query the database
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
table = Devices
deviceDict = queryRow(table)
print deviceDict
