from createDeviceChain import createChain 
from cplReadWrite import doStart, doStop, read

deviceList = createChain()
#opening all the threads
here = deviceList
while here != None:
    doStart(here)
    here = here.getNext()

#reading all the ports on the devices
for x in range(0,1):
    here = deviceList
    while here != None:
        try:
            print "Connecting to " + here.getObjectName()
            readDic = {}
            for item in range(1,len(here.getPort())+1):
                portObj = here.getPortItem(item)
                readDic[int(portObj.getPortNum())] = read(here, portObj)
            
        except Exception, e:
            print 'An error has occured: ' + str(e) + "\n"
        
        finally:
            print readDic
            here = here.getNext()

#claosing all the threads
#here = deviceList
#while here != None:
doStop()
#    here = here.getNext()
