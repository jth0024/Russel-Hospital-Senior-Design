from createDeviceChain import createChain 
#from DeviceRead2 import deviceRead
from cplReadWrite import doStart, doStop, read
from DeviceWrite import deviceWrite
import time
from fileToDic import fileToDic

for x in range(0,1):
    start = time.time()                     ################################
    deviceList = createChain()
    here = deviceList
    while here != None:
        try:
            started = doStart(here)
            #print started
            if started == True:
                #print "Started read 1..."
                start1 = time.time()            ################################
                readDic = {}
                for item in range(1,len(here.getPort())+1):
                    portObj = here.getPortItem(item)
                    #readDic[int(portObj.getPortNum())] = read(str(portObj.gettype()), int(portObj.getPortNum()), str(portObj.getvalue()))      
                    print str(portObj.gettype())
                end1 = time.time()              ################################
                #commit it to the databas
                #insertRow(valDic)
                #manipulate data
                start2 = time.time()            ################################
                #print "Started write ..."
                #writeDic = fileToDic('writeTest.txt')
                #deviceWrite(writeDic)       
                end2 = time.time()              ################################
                start3 = time.time()            ################################
               # print "Started read 2..."
                #valDic2 = deviceRead()
                end3 = time.time()              ################################
            else:
                print 'An error has been captured: ' + str(started) + ", " + here.getObjectName() + "\n"
                           
                
        except Exception, e:
            print 'An error has occured: ' + str(e) + "\n" 
           # doStop()
            started = False
        
        finally:
            if started == True:
                print "The first read took: " + str(end1 - start1) + " seconds"
                doStop()
                print readDic
                #print "The write took: " + str(end2 - start2) + " seconds"
                #print "The second read took: " + str(end3 - start3) + " seconds"
                print "The whole program took: " + str(end3 - start) + " seconds\n\n" 
            here = here.getNext()
