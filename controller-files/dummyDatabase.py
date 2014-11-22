import sys
sys.path.insert(0, '../database/database')
from sql_insert import insertNewRow
from sql_declarative import databaseCreation

print databaseCreation()
table = 'devices'
rowOne = {'name':'ControllerOne','ini':'ControllerOne.ini','ip':'192.168.92.69','mac':'macAddressOne'}
rowTwo = {'name':'ControllerTwo','ini':'ControllerTwo.ini','ip':'192.168.92.70','mac':'macAddressTwo'}

insertNewRow(table, rowOne)
insertNewRow(table, rowTwo)

tablename = 'setpoints'
setpointrow = {'tempSA':70,'tempMA':72,'tempPA':73,'tempSA':75,'humidityRA':20,'airFlowOA':25,'coRA':30}
insertNewRow(tablename, setpointrow)

