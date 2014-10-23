from createDeviceChain import createChain 
from cplReadWrite import doStart, doStop, read

deviceList = createChain()
here = deviceList#.getNext()

doStart(here)
readDic = {}
portObj = here.getPortItem(1)






