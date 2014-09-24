from iniParser import *
from Class import *


value = iniParser("BACpypes.ini")
value.append(CompIPToRequestIP(value[1]))

deviceList = Device(value[0],value[1],value[2],value[3],value[4],value[5],value[6],value[7],value[8],value[9])
