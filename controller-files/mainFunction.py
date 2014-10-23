from createDeviceChain import createChain 
from cplReadWrite import doStart, doStop, read
#from DeviceWrite import deviceWrite
import time
#from fileToDic import fileToDic

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
                 
                #commit it to the database
                #insertRow(valDic)
                
                #manipulate data
                for item in range(1,numberOfConnectedPorts):
                    portObj = here.getPortItem(item)
                    if portObj.getControlled():
                        manipulatedDic[portObj.getPortNum()] = portObj.Ploop(70, readDic[portObj.getPortNum()])
                    else:
                        manipulatedDic[portObj.getPortNum()] = None
            
            
            
            #    start2 = time.time()            ################################
                #print "Started write ..."
                #writeDic = fileToDic('writeTest.txt')
                #deviceWrite(writeDic)       
            #    end2 = time.time()              ################################

            else:
                print 'An error has been captured: ' + str(started) + ", " + here.getObjectName()  + "\n\n"
            
        except Exception, e:
            print 'An error has occured: ' + str(e) + "\n" 
            started = False
        
        finally:
            if started == True:
                doStop() 
                print "The first read took: " + str(end1 - start1) + " seconds"
                print readDic
                print manipulatedDic
                #print "The write took: " + str(end2 - start2) + " seconds"
                print "The whole program took: " + str(end2 - start) + " seconds\n\n" 
            here = here.getNext()
