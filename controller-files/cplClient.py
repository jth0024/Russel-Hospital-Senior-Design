#from cplReadWrite import read, write, doStop, doStart, addDevice, removeDevice, nextDevice
from cplMultipleApplications import read, createApplication, doStop
from createDeviceChain import createChain 
import time


deviceChain = createChain()
device = deviceChain


i = 0

while device != None:
	try:
		if i < 2:
			createApplication(device)
	except:
		print "Except: "
	finally:
		device = device.getNext()
		i += 1

	
for x in range(0,2):
	device = deviceChain
	i = 0	
	while device != None:

		print device.getObjectName()

		try:
			if i < 2:
				print "Try: "
				numberOfConnectedPorts = len(device.getPort())+1
				readDic = {}
				manipulatedDic = {}
				print "Preparing to read ports..."
				for item in range(1,numberOfConnectedPorts):
					portObj = device.getPortItem(item)
					readDic[item] = read(i, device, portObj)
					print "After Reading all ports: " + str(readDic)                 
	  
		except:
			print "Except: "
		finally:
			print "Finally: "
			device = device.getNext()
			i += 1

i = 0
device = deviceChain
while device != None and i < 2:
	doStop(i)
	i += 1
	device = device.getNext()

# obj_type = 'analogInput'
# obj_inst = int(2)
# prop_id = 'presentValue'
# ini_name = 'poop'

# doStart(ini_name)

# confirmationValue = read(obj_type, obj_inst, prop_id)
# print "Current Temperature: " + str(confirmationValue) + "\n"


# obj_type = 'analogOutput'
# obj_inst = int(3)
# value = float(2)
# index = int(0)
# priority = int(1)

# time.sleep(1)

# confirmationValue = write(obj_type, obj_inst, prop_id, value, index, priority)
# print "Write: " + str(confirmationValue)

# value = float(0)

# print "Lighting LED for 10 seconds\n"
# time.sleep(10)
# confirmationValue = write(obj_type, obj_inst, prop_id, value, index, priority)
# print "Write: " + str(confirmationValue)

# doStop()