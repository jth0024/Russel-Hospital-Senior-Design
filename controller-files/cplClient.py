#from cplReadWrite import read, write, doStop, doStart, addDevice, removeDevice, nextDevice
from cplMultipleApplications import read, createApplication, doStop
from createDeviceChain import createChain 
import time, os, subprocess


deviceChain = createChain()
device = deviceChain


i = 0

while device != None:
	try:
		# if i == 1:
		# 	createApplication(device)
		# else:
		# 	addDevice(device)
		if i < 2:
			createApplication(device)
	except:
		print "Except: "
	finally:
		device = device.getNext()
		i += 1

setpoint = 20
	
for x in range(0,1):
    device = deviceChain
    i = 0
    while device != None:
        
        print "Getting Ping..."
        ipAddress = device.getRequestAddress()
        
    #   with open(os.devnull, "wb") as limbo:
    #        result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ipAddress],
     #               stdout=limbo, stderr=limbo).wait()

#            if result:
#                print "Ping Failed for " + device.getObjectName()
#                started = False
                
#            else:
#                print "\nPing talked with" + device.getObjectName()
#                started = True
        
#        if started == True:
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
                
                
                #manipulate data
                for item in range(1,numberOfConnectedPorts):
                    portObj = device.getPortItem(item)
                    if portObj.getControlled():
                        #manipulatedDic should conatin the value from the Ploop with the key being the port of the actuator that the sensor is paired with
                        manipulatedDic[portObj.getConnectedTo()] = portObj.Ploop(setpoint, readDic[portObj.getPortNum()])     
                print "P-Loop result: " + str(manipulatedDic)
                        

                print "Started write ..."
                for item in manipulatedDic:
                    portObj = device.getPortItem(item)
                    write(device, portObj, manipulatedDic[item])      

    
        except:
            print "Except: "
        finally:
            print "Finally: "
            device = device.getNext()
            #print getDeviceByID(device.get)
            i += 1
    #

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
