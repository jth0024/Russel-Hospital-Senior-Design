# from createDeviceChain import createChain


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