import sys
sys.path.append('../database/database')
from iniParser import iniParser, CompIPToRequestIP, parsePorts
from Class import *
from sql_query import queryColumn 


#from sql_declarative import Devices


def createChain():
    iniName = queryColumn('devices', "ini")
    for index in range(0,len(iniName)):
        portDic = None
        deviceDic = None
        deviceDic = iniParser("iniFiles/" + str(iniName[index]))
        deviceDic['requestip'] = CompIPToRequestIP(deviceDic['address'])
        portDic = parsePorts("iniFiles/" + str(iniName[index]))

        for port in portDic:
            portDic[port] = instantiatePortClass(portDic[port], portNumber(port))

        if index == 0:
            deviceList = Device(deviceDic, portDic)
            counter = deviceList
        elif index ==1 :
            temp = Device(deviceDic, portDic)

            deviceList.addDevice(temp)
            counter = counter.getNext()    
                   
        else:
            temp = Device(deviceDic, portDic)
            counter.addDevice(temp)
            counter = counter.getNext()


    return deviceList



def instantiatePortClass(str_className,portNum):
    if str_className.lower() == "led":
        return DamperPositionOA(portNum)
    elif str_className.lower() == "thermistorcc":
        return TempSA(portNum, 1)
    elif str_className.lower() == "thermistorhc":
        return TempPA(portNum, 3)
    else:
        return "Error: Type not reconised"
    
    
def portNumber(str_portNum):
    if str_portNum.lower() == "portone":
        return 1
    elif str_portNum.lower() == "porttwo":
        return 2
    elif str_portNum.lower() == "portthree":
        return 3     
    elif str_portNum.lower() == "portfour":
        return 4    
    elif str_portNum.lower() == "portfive":
        return 5
    elif str_portNum.lower() == "portsix":
        return 6
    elif str_portNum.lower() == "portseven":
        return 7
    elif str_portNum.lower() == "porteight":
        return 8
    elif str_portNum.lower() == "portnine":
        return 9
