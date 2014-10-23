from createDeviceChain import createChain 
from cplReadWrite import doStart, doStop, read, write
import time

# STILL NEED TO DO ERROR CHECKING FOR WHOLE PROGRAM

setpoint = 70


for x in range(0,1):
    start = time.time()                     ################################
    deviceList = createChain()
    here = deviceList
    while here != None:
        try:
            print "Connecting to " + here.getObjectName()
            started = doStart(here)
            if started == True:
                start1 = time.time()            ################################
                numberOfConnectedPorts = len(here.getPort())+1
                readDic = {}
                manipulatedDic = {}
                
                # Reading all ports on device
                for item in range(1,numberOfConnectedPorts):
                    portObj = here.getPortItem(item)
                    readDic[int(portObj.getPortNum())] = read(here, portObj)
                end1 = time.time()              ################################
                print "After Reading all ports: " + str(readDic)                 
                #commit it to the database
                #insertRow(valDic)
                
                #manipulate data
                for item in range(1,numberOfConnectedPorts):
                    portObj = here.getPortItem(item)
                    if portObj.getControlled():
                        manipulatedDic[portObj.getConnectedTo()] = portObj.Ploop(setpoint, readDic[portObj.getPortNum()])     #manipulatedDic should conatin the value from the Ploop with the key being the port of the actuator that the sensor is paired with
                print "after Ploop : " + str(manipulatedDic)
            
            #temporary fix for working with LED and not actual actuators
                for value in manipulatedDic:
                    if manipulatedDic[value] < 0:
                        manipulatedDic[value] = 0.0
                    elif manipulatedDic[value] > 4:
                        manipulatedDic[value] = 4.0
                print "after correction for LED : " + str(manipulatedDic)
  
                        
                start2 = time.time()            ################################
                #print "Started write ..."
                for item in manipulatedDic:
                    portObj = here.getPortItem(item)
                    write(here, portObj, manipulatedDic[item])      
                end2 = time.time()              ################################

            
            
            else:
                print 'An error has been captured: ' + str(started) + ", " + here.getObjectName()  + "\n\n"
            
        except Exception, e:
            print 'An error has occured: ' + str(e) + "\n" 
            started = False
        
        finally:
            if started == True:
                doStop() 
                print "The first read took: " + str(end1 - start1) + " seconds"
                print "The write took: " + str(end2 - start2) + " seconds"
                print "The whole program took: " + str(end2 - start) + " seconds\n\n" 
            here = here.getNext()
