import sys
sys.path.append('../database-files')
from iniParser import iniParser, CompIPToRequestIP
from Class import Device
from sql_query import queryColumn 
from sql_declarative import Devices

def createChain():
    iniName = queryColumn(Devices, "ini")
    for x in range(0,len(iniName)):
        value = iniParser("iniFiles/" + str(iniName[x]))
        value.append(CompIPToRequestIP(value[1]))
        if x == 0:
            deviceList = Device(value[0],value[1],value[2],value[3],value[4],value[5],value[6],value[7],value[8],value[9])
            counter = deviceList
        elif x ==1 :
            temp = Device(value[0],value[1],value[2],value[3],value[4],value[5],value[6],value[7],value[8],value[9])
            deviceList.addDevice(temp)
            counter = counter.getNext()
        else:
            temp = Device(value[0],value[1],value[2],value[3],value[4],value[5],value[6],value[7],value[8],value[9])
            counter.addDevice(temp)
            counter = counter.getNext()
            
    return deviceList
