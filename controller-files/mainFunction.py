from createDeviceChain import createChain 
from DeviceRead2 import deviceRead
from cplReadWrite import doStart, doStop
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
                valDic = deviceRead()
                end1 = time.time()              ################################
                #commit it to the databas
                #insertRow(valDic)
                #manipulate data
                start2 = time.time()            ################################
                #print "Started write ..."
                writeDic = fileToDic('writeTest.txt')
                deviceWrite(writeDic)       
                end2 = time.time()              ################################
                start3 = time.time()            ################################
               # print "Started read 2..."
                #valDic2 = deviceRead()
                end3 = time.time()              ################################
            else:
                print 'An error has been captured: ' + str(started) + ", " + here.getObjectName() + "\n"
                
                
        except Exception, e:
            print 'An error has occured: ' + str(e) + "\n" 
            doStop()
            started = False
        
        finally:
            if started == True:
                doStop()
                #print "The first read took: " + str(end1 - start1) + " seconds"
                print valDic
                #print "The write took: " + str(end2 - start2) + " seconds"
                #print "The second read took: " + str(end3 - start3) + " seconds"
                #print "The whole program took: " + str(end3 - start) + " seconds" 
            here = here.getNext()

            
    #print valDic
