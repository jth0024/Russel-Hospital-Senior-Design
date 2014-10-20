import sys
sys.path.append('../database/database')
from iniParser import iniParser, CompIPToRequestIP, parsePorts
from Class import *
from sql_query import queryColumn 


#from sql_declarative import Devices


def createChain():
    iniName = queryColumn('Devices', "ini")
    for index in range(0,len(iniName)):
        portDic = None
        deviceDic = None
        print "\n" +iniName[index]
        print portDic
        deviceDic = iniParser("iniFiles/" + str(iniName[index]))
        deviceDic['requestip'] = CompIPToRequestIP(deviceDic['address'])
        portDic = parsePorts("iniFiles/" + str(iniName[index]))  #Still reads [Ports] information even if nothing is in file, not sure how to fix
        print portDic

        for port in portDic:
            portDic[port] = instantiatePortClass(portDic[port], portNumber(port))

        if index == 0:
            deviceList = Device(deviceDic, portDic)
#            deviceList = Device(dictionary['objectname'],dictionary['address'],
#            dictionary['objectidentifier'],dictionary['maxapdulengthaccepted'],
#            dictionary['segmentationsupported'],dictionary['vendoridentifier'],
#            dictionary['foreignport'],dictionary['foreignbbmd'],
#            dictionary['foreignttl'],dictionary['requestip'])
            counter = deviceList
        elif index ==1 :
            temp = Device(deviceDic, portDic)
#            temp = Device(dictionary['objectname'],dictionary['address'],
#            dictionary['objectidentifier'],dictionary['maxapdulengthaccepted'],
#            dictionary['segmentationsupported'],dictionary['vendoridentifier'],
#            dictionary['foreignport'],dictionary['foreignbbmd'],
#            dictionary['foreignttl'],dictionary['requestip'])
            deviceList.addDevice(temp)
            counter = counter.getNext()
#           
        else:
            temp = Device(deviceDic, portDic)
#            temp = Device(dictionary['objectname'],dictionary['address'],
#            dictionary['objectidentifier'],dictionary['maxapdulengthaccepted'],
#            dictionary['segmentationsupported'],dictionary['vendoridentifier'],
#            dictionary['foreignport'],dictionary['foreignbbmd'],
#            dictionary['foreignttl'],dictionary['requestip'])
            counter.addDevice(temp)
            counter = counter.getNext()



        # value = iniParser("iniFiles/" + str(iniName[x]))
        # value['requestAddress'] = str(CompIPToRequestIP(value[1]))
        # if x == 0:
        #     deviceList = Device(value['objectName'],value['address'],
        #     value['objectIdentifier'],value['maxApduLengthAccepted'],
        #     value['segmentationSupported'],value['vendorIdentifier'],
        #     value['foreignPort'],value['foreignBBMD'],
        #     value['foreignTTL'],value['requestAddress'])
        #     counter = deviceList
        # elif x ==1 :
        #     temp = Device(value['objectName'],value['address'],
        #     value['objectIdentifier'],value['maxApduLengthAccepted'],
        #     value['segmentationSupported'],value['vendorIdentifier'],
        #     value['foreignPort'],value['foreignBBMD'],
        #     value['foreignTTL'],value['requestAddress'])
        #     deviceList.addDevice(temp)
        #     counter = counter.getNext()
        # else:
        #     temp = Device(value['objectName'],value['address'],
        #     value['objectIdentifier'],value['maxApduLengthAccepted'],
        #     value['segmentationSupported'],value['vendorIdentifier'],
        #     value['foreignPort'],value['foreignBBMD'],
        #     value['foreignTTL'],value['requestAddress'])

    return deviceList



def instantiatePortClass(str_className,portNum):
    if str_className.lower() == "led":
        return DamperPositionOA(portNum)
    elif str_className.lower() == "thermistor":
        return TempPA(portNum)
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
