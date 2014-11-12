from cplReadWrite import read, write, doStop, doStart, addDevice, removeDevice, nextDevice
from createDeviceChain import createChain 
import time

deviceChain = createChain()
device = deviceChain


i = 1

while device != None:
	try:
		if i == 1:
			doStart(device)
		else:
			addDevice(device)
	except:
		print "Except: "
	finally:
		device = device.getNext()
		i += 1
for x in range(0,2):
	device = deviceChain

	while device != None:

		print device.getObjectName()

		try:
			print "Try: "
			numberOfConnectedPorts = len(device.getPort())+1
			readDic = {}
			manipulatedDic = {}
			for item in range(1,numberOfConnectedPorts):
				portObj = device.getPortItem(item)
				readDic[item] = read(device, portObj)
				print "After Reading all ports: " + str(readDic)                 
	  
		except:
			print "Except: "
		finally:
			print "Finally: "
			device = device.getNext()
			nextDevice()

		
doStop()

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