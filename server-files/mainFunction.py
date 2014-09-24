from fileToDic import fileToDic
from DeviceRead2 import deviceRead
from cplReadWrite import doStart, doStop
from DeviceWrite import deviceWrite
import time


for x in range(0,3):
    start = time.time()                     ################################
    deviceDic = fileToDic('DeviceList.txt')
    #print deviceDic
    for Key in deviceDic:
        try:
            started = doStart(deviceDic[Key])
            #print started
            if started == True:
                #for x in range (0,10):
                 #   print "trial " + str(x) + ":\n"
                start1 = time.time()            ################################
                valDic = deviceRead()
                end1 = time.time()              ################################
                #commit it to the databas
                insertRow(valDic)
                #manipulate data
                start2 = time.time()            ################################
                writeDic = fileToDic('writeTest.txt')
                deviceWrite(writeDic)       
                end2 = time.time()              ################################
                start3 = time.time()            ################################
                valDic2 = deviceRead()
                end3 = time.time()              ################################
            else:
                print 'An error has been captured: ' + str(started) +", "+ deviceDic[Key] + "\n"
        except Exception, e:
            print 'An error has Accured: ' + str(e) + "\n" 
        
        finally:
            if started == True:
                doStop()
                print "The first read took: " + str(end1 - start1) + " seconds"
                print valDic
                print "The write took: " + str(end2 - start2) + " seconds"
                print "The second read tool: " + str(end3 - start3) + " seconds"
                print "The whole program took: " + str(end3 - start) + " seconds" 
    #print valDic
