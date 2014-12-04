from readWrite import read, write, createApplication, doStop
from createDeviceChain import createChain 
from sql_insert import insertNewRow
import time, os, subprocess



#deviceChain holds a pointer to the start of the singly linked list of device objects
deviceChain = createChain()
#device is used to iterate through the linked list
device = deviceChain

#this is a hard coded value right now but  will need to be changed so that it gets the setpoint from a database table.
setpoint = 72


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

#This outer for loop determines how many times we ask the devices for information. Eventually this will be and infinite loop
#All of the print statements are here for diagnostic reasons. They will be removed from the final product
for x in range(0,2):
	device = deviceChain
	i = 0	
	while device != None:

		print device.getObjectName()  #Prints what device you are talking with, i.e. controller one

		try:
			numberOfConnectedPorts = len(device.getPort())+1
			print "numberOfConnectedPorts: " + str(numberOfConnectedPorts)
			#these are the values read from the controller
			readDic = {}
			#These are the values that the output is set to based on the controllLoop function
			manipulatedDic = {}
			
			#Reading each port on the device and storing in the readDic with the port number as the key
			print "Preparing to read ports..."
			for item in range(1,numberOfConnectedPorts):
				portObj = device.getPortItem(item)
				readDic[item] = read(i, device, portObj)
			print "After Reading all ports: " + str(readDic)  #display the read values

			#Determining the correct output from the controller. ManipulatedDic should contain the value from the P-loop with the key being the port of the actuator that the sensor is paired with
			for item in range(1,numberOfConnectedPorts):
				portObj = device.getPortItem(item)
				if portObj.getControlled():
					print readDic[portObj.getPortNum()]
					manipulatedDic[portObj.getConnectedTo()] = portObj.Ploop(setpoint, readDic[portObj.getPortNum()])     
			print "P-Loop result: " + str(manipulatedDic)

			#Write the new output values to the controller.
			for item in manipulatedDic:
				portObj = device.getPortItem(item)
				write(i, device, portObj, manipulatedDic[item])
		except ValueError:
			print "Except: " + str(ValueError)
		finally:
			#gets the next device in the linked list
			device = device.getNext()
			i += 1

time.sleep(1.5)

print "Stopping applications..."
i = 0
device = deviceChain
while device != None:
	doStop(i)
	i += 1
	device = device.getNext()

