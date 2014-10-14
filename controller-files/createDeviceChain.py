import sys
sys.path.append('../database/database')
from iniParser import iniParser, CompIPToRequestIP
from Class import Device
from sql_query import queryColumn 
<<<<<<< HEAD
=======
#from sql_declarative import Devices
>>>>>>> FETCH_HEAD

def createChain():
    iniName = queryColumn('Devices', "ini")
    for x in range(0,len(iniName)):
<<<<<<< HEAD
        dictionary = iniParser("iniFiles/" + str(iniName[x]))
        dictionary['RequestIP'] = CompIPToRequestIP(dictionary['address'])
        if x == 0:
            deviceList = Device(dictionary['objectName'],dictionary['address'],dictionary['objectIdentifier'],dictionary['maxApduLengthAccepted'],dictionary['segmentationSupported'],dictionary['vendorIdentifier'],dictionary['foreignPort'],dictionary['foreignBBMD'],dictionary['foreignTTL'],dictionary['RequestIP'])
            counter = deviceList
        elif x ==1 :
            temp = Device(dictionary['objectName'],dictionary['address'],dictionary['objectIdentifier'],dictionary['maxApduLengthAccepted'],dictionary['segmentationSupported'],dictionary['vendorIdentifier'],dictionary['foreignPort'],dictionary['foreignBBMD'],dictionary['foreignTTL'],dictionary['RequestIP'])
            deviceList.addDevice(temp)
            counter = counter.getNext()
        else:
            temp = Device(dictionary['objectName'],dictionary['address'],dictionary['objectIdentifier'],dictionary['maxApduLengthAccepted'],dictionary['segmentationSupported'],dictionary['vendorIdentifier'],dictionary['foreignPort'],dictionary['foreignBBMD'],dictionary['foreignTTL'],dictionary['RequestIP'])
=======
        value = iniParser("iniFiles/" + str(iniName[x]))
        value['requestAddress'] = str(CompIPToRequestIP(value[1]))
        if x == 0:
            deviceList = Device(value['objectName'],value['address'],
            value['objectIdentifier'],value['maxApduLengthAccepted'],
            value['segmentationSupported'],value['vendorIdentifier'],
            value['foreignPort'],value['foreignBBMD'],
            value['foreignTTL'],value['requestAddress'])
            counter = deviceList
        elif x ==1 :
            temp = Device(value['objectName'],value['address'],
            value['objectIdentifier'],value['maxApduLengthAccepted'],
            value['segmentationSupported'],value['vendorIdentifier'],
            value['foreignPort'],value['foreignBBMD'],
            value['foreignTTL'],value['requestAddress'])
            deviceList.addDevice(temp)
            counter = counter.getNext()
        else:
            temp = Device(value['objectName'],value['address'],
            value['objectIdentifier'],value['maxApduLengthAccepted'],
            value['segmentationSupported'],value['vendorIdentifier'],
            value['foreignPort'],value['foreignBBMD'],
            value['foreignTTL'],value['requestAddress'])
>>>>>>> FETCH_HEAD
            counter.addDevice(temp)
            counter = counter.getNext()
            
    return deviceList
