#!./BACpypesEnv/bin/python

#import sys

#Import BACpypes Stuff
from bacpypes.core import run, stop
from bacpypes.app import LocalDeviceObject, BIPSimpleApplication
from bacpypes.basetypes import ServicesSupported
from threading import Thread
from bacpypes.apdu import ReadPropertyRequest, Error, AbortPDU, ReadPropertyACK, SimpleAckPDU, WritePropertyRequest
from bacpypes.pdu import Address
from bacpypes.object import get_datatype, get_object_class
from bacpypes.constructeddata import Any
from bacpypes.primitivedata import Real

#random imports
import time 




#Application Globals
this_device = None
this_application = None
has_started = True
request_addr = None
applicationThread = None





#BACnet Application definition, mostly needed for custom 'Confirmation' behavior
class Application(BIPSimpleApplication):

    def __init__(self, device, address):
        print 'Initializing BACpypes Service...\n'
        BIPSimpleApplication.__init__(self, device, address)
        self.__response_value = None
    
    def request(self, apdu):
    	print 'Passing along request...\n'
        self.__response_value = None
        BIPSimpleApplication.request(self, apdu)

    def indication(self, apdu):
        BIPSimpleApplication.indication(self, apdu)

    def response(self, apdu):
        BIPSimpleApplication.response(self, apdu)

    def confirmation(self, apdu):
        #Executed when a packet is recieved (not just a BACnet packet)
        try:
            if isinstance(apdu, ReadPropertyACK):
	        	#print "Current Temperature: " + str(apdu.propertyValue.cast_out(Real)) + "\n"
	        	self.__response_value = apdu.propertyValue.cast_out(Real)
            elif isinstance(apdu, SimpleAckPDU):
	        	self.__response_value = "Ack\n"
            elif isinstance(apdu, AbortPDU):
	        	print "apdu: " + str(apdu.apduAbortRejectReason) + "\n"
            elif isinstance(apdu, Error):
	        	print "apdu: " + str(apdu) + "\n"
	        	
        except Exception, e:
            print 'An error has been detained: ' + str(has_started) +", "+ str(e) + "\n"
    #__return_value = None

class BACpypeThread(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        Thread.name = name
    def run(self):
        run()
    def stop(self):
        stop()      

def doStop():
	stop()
	applicationThread.join()

def read(obj_type, port, prop_id):

	try: 
		#--------------------------read property request
		#verify datatype
		print "Reading..."
		print obj_type, port, prop_id
		
		if obj_type.isdigit():
		    obj_type = int(obj_type)
		elif not get_object_class(obj_type):
		    raise ValueError, "unknown object type"
		    
		          
		datatype = get_datatype(obj_type, prop_id)
		if not datatype:
			print ValueError, ": invalid property for object type"
		
		port = int(port)	
		
		#build request
		request = ReadPropertyRequest(
		    objectIdentifier=(obj_type, port), 
		    propertyIdentifier=prop_id,
		    )
		request.pduDestination = Address(request_addr)
		
		#submit request
		
		print request.pduDestination
		
		
		this_application.request(request)
		print "Waiting for reply..."
		#wait for request
		wait = 0
		while this_application._Application__response_value == None:
		    wait = wait + .01
		    time.sleep(.01)
		returnVal = this_application._Application__response_value
        
        
	except Exception, e:
		returnVal = None
		print 'An error has happened (CPLRW 127): ' + str(e) + "\n"

	finally:
	    #print "the total wait time was: " + str(wait) + " seconds"
	    return returnVal

def write(obj_type, obj_inst, prop_id, value, index, priority):

	try:
		#verify datatype
		datatype = get_datatype(obj_type, prop_id)
		if not datatype:
			raise ValueError, ": invalid property for object type"
		value = datatype(value)
		request = WritePropertyRequest(objectIdentifier=(obj_type, obj_inst), propertyIdentifier=prop_id)
		request.pduDestination = Address(request_addr)
		request.propertyValue = Any()
		request.propertyValue.cast_in(value)
		request.propertyArrayIndex = index
		request.priority = priority
		this_application.request(request)
		time.sleep(.1)
		returnVal = this_application._Application__response_value
	except:
		returnVal = "Error, unable to write"

	finally:
		return returnVal

def doStart(device):
	global this_application, this_device, applicationThread, request_addr, has_started
	has_started = True
	try:
		#args = ConfigArgumentParser(description=__doc__).parse_args()

		#Defining Device
		this_device = LocalDeviceObject(
	    	objectName=device.getObjectName(),
	    	objectIdentifier=int(device.getObjectIdentifier()),
	    	maxApduLengthAccepted=int(device.getMaxApduLengthAccepted()),
	    	segmentationSupported=device.getSegmentationSupported(),
	    	vendorIdentifier=int(device.getVendorIdentifier()),
	    	)
		
		print 
		
		
		request_addr = device.getRequestAddress()

		pss = ServicesSupported()
		pss['whoIs'] = 1
		pss['iAm'] = 1
		pss['readProperty'] = 1
		pss['writeProperty'] = 1

		this_device.protocolServicesSupported = pss.value 

		this_application = Application(this_device, device.getDeviceAddress())
		print "this Addr:" + str(device.getDeviceAddress())
		#Start BACpypes Thread
		applicationThread = BACpypeThread('BACPYPE-APP')
		applicationThread.start()

	except Exception:
		has_started = False
	
	finally:
		#print "Finally\n"
		return has_started


