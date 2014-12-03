import sys
sys.path.insert(0, '../database/database')
from sql_insert import insertNewRow
from sql_declarative import databaseCreation
from sql_query import queryTable

print databaseCreation()
table = 'devices'
rowOne = {'name':'ControllerOne','ini':'ControllerOne.ini','ip':'192.168.92.69','mac':'macAddressOne'}
rowTwo = {'name':'ControllerTwo','ini':'ControllerTwo.ini','ip':'192.178.92.79','mac':'macAddressTwo'}

insertNewRow(table, rowOne, 'sqlite:///../database/database/rh.db')
insertNewRow(table, rowTwo, 'sqlite:///../database/database/rh.db')

tablename = 'setpoints'
setpointrow = {'tempSA':70,'tempMA':72,'tempPA':73,'tempSA':75,'humidityRA':20,'airFlowOA':25,'coRA':30}
insertNewRow(tablename, setpointrow)


