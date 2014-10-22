from createDeviceChain import createChain 
from cplReadWrite import doStart, doStop, read

deviceList = createChain()
here = deviceList#.getNext()

doStart(here)
readDic = {}
portObj = here.getPortItem(1)
print portObj
readDic[int(portObj.getPortNum())] = read(str(portObj.gettype()), int(portObj.getPortNum()), str(portObj.getvalue()))

doStop()

print readDic

