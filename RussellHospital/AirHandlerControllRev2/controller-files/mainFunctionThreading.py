from createDeviceChain import createChain 
from cplReadWrite import doStart, doStop, read, write
import time, sys
from ErrorClasses import *

# STILL NEED TO DO ERROR CHECKING FOR WHOLE PROGRAM

setpoint = 20

deviceList = createChain()
here = deviceList
while here != None:
    doStart(here)
    here = here.getNext()

time.sleep(3)

for x in range(0,1):
    start = time.time()                     ################################
    
    here = deviceList
    while here != None:
        try:
            print "Connecting to " + here.getObjectName()
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
            

            
        except ComputerNotConnectedToIP, exc:
            print exc 
        
        except Exception, e:    
            print "You found a new error. Congrats!:" + str(e)
        
        finally:
            print "The first read took: " + str(end1 - start1) + " seconds"
            here = here.getNext()
            
doStop()    
            
            
