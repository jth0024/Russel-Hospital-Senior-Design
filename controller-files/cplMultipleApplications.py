#!./BACpypesEnv/bin/python

#Import BACpypes Stuff
from bacpypes.core import run, stop
from bacpypes.app import LocalDeviceObject, BIPSimpleApplication
from bacpypes.basetypes import ServicesSupported
import threading
from threading import Thread
from bacpypes.apdu import ReadPropertyRequest, Error, AbortPDU, ReadPropertyACK, SimpleAckPDU, WritePropertyRequest
from bacpypes.pdu import Address
from bacpypes.object import get_datatype, get_object_class
from bacpypes.constructeddata import Any
from bacpypes.primitivedata import Real

#random imports
import time 
from ErrorHandler import ErrorHandler


#Application Globals
#contains all our applications
applications = list()
applicationCount = 0





#BACnet Application definition, mostly needed for custom 'Confirmation' behavior
class Application(BIPSimpleApplication):

	def __init__(self, device, address):
		#print 'Initializing BACpypes Service...'
		BIPSimpleApplication.__init__(self, device, address)
	
	def request(self, apdu):
		#print 'Passing along request...'
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

def doStop(appIndex):
	#threading.currentThread().join()
	global applications
	application = applications[appIndex]
	stop()

# def addDevice(device):
#     global this_application
#     #Defining Device
#     localDevice = LocalDeviceObject(
#         objectName=device.getObjectName(),
#         objectIdentifier=int(device.getObjectIdentifier()),
#         maxApduLengthAccepted=int(device.getMaxApduLengthAccepted()),
#         segmentationSupported=device.getSegmentationSupported(), 
#         vendorIdentifier=int(device.getVendorIdentifier()),
#         )    
#     this_application.add_object(localDevice)

# def removeDevice(device):
#     global this_application
#     this_application.delete_object(device)

# def nextDevice():
#     global this_application
#     return this_application.iter_objects()

def getDeviceByID(appIndex, deviceID):
	return applications[appIndex].get_object_id(deviceID)

def read(appIndex, device, portObject): 
	global applications
	application = applications[appIndex]
	request_addr = device.getRequestAddress()
	obj_type = portObject.getType()
	port = portObject.getPortNum()
	prop_id = portObject.getProp()
	maximumWait = 6  #seconds

	try:
		#Jordan Trying to open thread in application

		#--------------------------read property request
		#verify datatype
		print "Reading..."
		print request_addr, obj_type, port, prop_id
		
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
		time.sleep(.01)  #I dont know why, but this makes the code work correctly.
		#submit request
		application.request(request)

		wait = 0
		while application._Application__response_value == None and wait <= maximumWait:
			wait = wait + .01
			time.sleep(.01)
		returnVal = application._Application__response_value
	except Exception, e:
		returnVal = None
		print 'An error has happened (CPLRW 126): ' + str(e) + "\n"
		
	finally:
		#print "the total wait time was: " + str(wait) + " seconds" 
		return returnVal



# def write(device, portObject, value):
#     request_addr = device.getRequestAddress()
#     obj_type = portObject.getType()
#     obj_inst = portObject.getPortNum()
#     prop_id = portObject.getProp()
#     index = portObject.getIndex()
#     priority = portObject.getPriority()

#     try:
#         #verify datatype
#         datatype = get_datatype(obj_type, prop_id)
#         if not datatype:
#             raise ValueError, ": invalid property for object type"
#         value = datatype(value)
#         request = WritePropertyRequest(objectIdentifier=(obj_type, obj_inst), propertyIdentifier=prop_id)
#         request.pduDestination = Address(request_addr)
#         request.propertyValue = Any()
#         request.propertyValue.cast_in(value)
#         request.propertyArrayIndex = index
#         request.priority = priority
#         this_application.request(request)
#         time.sleep(.1)
#         returnVal = this_application._Application__response_value
#     except:
#         returnVal = "Error, unable to write"
	
#     finally:
#         return returnVal
	
def createApplication(device):
	global applicationCount, applications
	try:
		print 1
		#Defining Device
		threadName = 'app_' + str(applicationCount)
		localDevice = LocalDeviceObject(
			objectName=device.getObjectName(),
			objectIdentifier=int(device.getObjectIdentifier()),
			maxApduLengthAccepted=int(device.getMaxApduLengthAccepted()),
			segmentationSupported=device.getSegmentationSupported(), 
			vendorIdentifier=int(device.getVendorIdentifier()),
			)
		print 2
		pss = ServicesSupported()
		pss['whoIs'] = 1
		pss['iAm'] = 1
		pss['readProperty'] = 1
		pss['writeProperty'] = 1
		print 3
		localDevice.protocolServicesSupported = pss.value
		application = Application(localDevice, device.getDeviceAddress())
		print 4
		applications.append(application)
		applicationThread = BACpypeThread(threadName)
		applicationThread.start()
		print 5
		print "\n"
		applicationCount += 1
	
	except Exception, e:
		print "Error: doStart()"
		ErrorHandler(e,device)

#def startApplication(appIndex)
	#applicationThread = BACpypeThread('BACPYPE-APP')
	#applicationThread.start()
