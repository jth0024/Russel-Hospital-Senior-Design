"""
MotherShip Code
Code is based of the BACpypes example WhoIsIAm.py. Main purpose of the code is to ping all devices and to make a list of all 
responding devices and get their data values

GitHub description:
Added code to import expect device list from data base, code to make a list of devices responding using the confirmation method in WhoIsIAmApplication, and compares the two list. Not using the correct names for reading and writing from the databases.
"""

#Imports BACpypes commands
import sys

from bacpypes.debugging import bacpypes_debugging, ModuleLogger
from bacpypes.consolelogging import ConfigArgumentParser
from bacpypes.consolecmd import ConsoleCmd

from bacpypes.core import run

from bacpypes.pdu import Address, GlobalBroadcast
from bacpypes.app import LocalDeviceObject, BIPSimpleApplication

from bacpypes.apdu import WhoIsRequest, IAmRequest
from bacpypes.basetypes import ServicesSupported
from bacpypes.errors import DecodingError

#Imports various commands
import time
import datetime
import socket
import os
import sqlite3
import ConfigParser

# globals
this_device = None
this_application = None

class WhoIsIAmApplication(BIPSimpleApplication):

    def __init__(self, *args):
        BIPSimpleApplication.__init__(self, *args)
        # keep track of requests to line up responses
        self._request = None

    def request(self, apdu):
        # save a copy of the request
        self._request = apdu
        # forward it along
        BIPSimpleApplication.request(self, apdu)

    def confirmation(self, apdu):
    	#Upon confirmation of a packet being received, code makes a list of devices responding
    	try:
            #Check that it is a BACnet packet
            if isinstance(apdu,ReadPropertyACK):
                #Import Global Variabled to report back number of packets recieved
                global NumberOfDevices 
                global ExpectedDevices
                global FoundDevices

                #Get object type and instance from packet
                types= str(apdu.objectIdentifier[0])
                instances = int(apdu.objectIdentifier[1])

                #Look of responding device in objects list to both notify the main script that it 
                #has responded and to load its properties.
                for o in range(0,len(objects)):

                    obj = ExpectedDevices[o]
                    typ = str(obj['Type'])
                    inst = int(obj['Instance'])

                    if typ==types and inst==instances:
                        FoundDevices.append(o)
                        device = ExpectedDevices[o]
                        NumberOfDevices = NumberOfDevices + 1

                #Commit to Database--------------------------Added into for loop for multiple devices
                #Change variables to ones that will be put into database, should data be here?
                		Reading = device['Name']
                		Data = apdu.propertyValue.cast_out(Real)
                		Time = datetime.datetime.now()
                		Equip = device['Equipment']
                		EquipType = device['Equipment Type']
                		ddb = sqlite3.connect('NameofDB.db')
               			dc = ddb.cursor()
                		dc.execute('Insert into Data(SystemType,System,Time,Reading,Data) values(?,?,?,?,?)',(EquipType,Equip,Time,Reading,Data))
                		ddb.commit()
                		ddb.close()

        except Exception, e:
            log('Confirmation Error'+str(e))

        # forward it along,--------------------------is this needed?
        BIPSimpleApplication.confirmation(self, apdu)

    def indication(self, apdu):
        if (isinstance(self._request, WhoIsRequest)) and (isinstance(apdu, IAmRequest)):
            device_type, device_instance = apdu.iAmDeviceIdentifier
            if device_type != 'device':
                raise DecodingError, "invalid object type"

            if (self._request.deviceInstanceRangeLowLimit is not None) and \
                (device_instance < self._request.deviceInstanceRangeLowLimit):
                pass
            elif (self._request.deviceInstanceRangeHighLimit is not None) and \
                (device_instance > self._request.deviceInstanceRangeHighLimit):
                pass
            else:
                # print out the contents
                sys.stdout.write('pduSource = ' + repr(apdu.pduSource) + '\n')
                sys.stdout.write('iAmDeviceIdentifier = ' + str(apdu.iAmDeviceIdentifier) + '\n')
                sys.stdout.write('maxAPDULengthAccepted = ' + str(apdu.maxAPDULengthAccepted) + '\n')
                sys.stdout.write('segmentationSupported = ' + str(apdu.segmentationSupported) + '\n')
                sys.stdout.write('vendorID = ' + str(apdu.vendorID) + '\n')
                sys.stdout.flush()

        # forward it along
        BIPSimpleApplication.indication(self, apdu)


#Convert SQLite query results to dictionary
def dict_factory(cursor, row):
    d = {}
    for idx,col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

"""
#Looks at device table in database to get a list of expected devices
#Change to correct database, find out how to call a table in a database
db = sqlite3.connect('Devices.db')
    with db:
        db.row_factory=dict_factory
        cur = db.cursor()
        cur.execute("select * from objects")
        ExpectedDevices = cur.fetchall()
"""

"""
#Makes a list of devices that failed to connect despite being expected
#Commites missing list of devices to ????
MissingList = list(set(ExpectedDevices) - set(AcutalDevices))
MissingString = ""
for i in range(0,len(MissingList)):
	MissingString = MissingString + " " + str(MissingList[i]) 
print ("The following devices did not respond:" + MissingString)
"""
