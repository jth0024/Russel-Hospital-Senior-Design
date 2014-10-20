<<<<<<< HEAD
# from createDeviceChain import createChain
=======
from iniParser import parsePorts
>>>>>>> FETCH_HEAD

helps = parsePorts("iniFiles/ControllerOne.ini")
help = parsePorts("iniFiles/ControllerFour.ini")

<<<<<<< HEAD
# devices = createChain()

# print devices.getPortItem(2).getPortNum()

from iniParser import iniParser, parsePorts

deviceDic = parsePorts("iniFiles/ControllerTwo.ini")
print deviceDic
deviceDic2 = parsePorts("iniFiles/ControllerThree.ini")
print deviceDic2
deviceDic3 = parsePorts("iniFiles/ControllerFour.ini")
print deviceDic3
deviceDic4 = parsePorts("iniFiles/ControllerOne.ini")
print deviceDic4
=======
print help
print helps
print len(help)

for item in range(1,len(help)+1):
    print help.getPortItem(item)

>>>>>>> FETCH_HEAD
