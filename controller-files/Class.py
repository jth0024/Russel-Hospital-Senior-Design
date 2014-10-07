
class AnalogInput(object):
	
	def __init__(self):
	    self._type = 'analogInput'
	    self._value = 'presentValue'

	def gettype(self):
		return self._type
	def getvalue(self):
		return self._value
	def settype(self,type):
		self._type = type
	def setValue(self,value):
		self._value = value	
class AnalogOutput(object):
	type = 'analogOutput'
	value = 'presentValue'
	index = 0
	priority = 1

	def gettype(self):
		return self.type
	def getvalue(self):
		return self.value
	def getindex(self):
		return self.index
	def getpriority(self):
		return self.priority
	def settype(self,type):
		self.type = type
	def setValue(self,value):
		self.value = value
	def selfindex(self, index):
		self.index = index
	def selfpriority(self, priority):
		self.priority = priority

class DigitalInput(object):
	type = 'digitalInput'
	value = 'presentValue'

	def gettype(self):
		return self.type
	def getvalue(self):
		return self.value
	def settype(self,type):
		self.type = type
	def setValue(self,value):
		self.value = value	
class DigitalOutput(object):
	type = 'digitalOutput'
	value = 'presentValue'
	index = 0
	priority = 1

	def gettype(self):
		return self.type
	def getvalue(self):
		return self.value
	def getindex(self):
		return self.index
	def getpriority(self):
		return self.priority
	def settype(self,type):
		self.type = type
	def setValue(self,value):
		self.value = value
	def selfindex(self, index):
		self.index = index
	def selfpriority(self, priority):
		self.priority = priority	


class ControlLoop(object):
	def Ploop(self, setpoint,currentValue,pValue):
		outputValue = pValue*(setpoint-currentValue)
		return outputValue
	def PIloop(self, setpoint,currentValue,pValue,iValue):
		outputValue = 'Insert control eqation here'
		return outputValue
	def PIDloop(self, setpoint,currentValue,pValue,iValue,dValue):
		outputValue = 'Insert control eqation here'
		return outputValue


### Inputs
#add name field

class TempMA(AnalogInput,ControlLoop):
    def __init__(self, port):
        self._portNum = port
        pValue = 2.3
        iValue = 4
        dValue = 3
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class TempPA(AnalogInput,ControlLoop):
    def __init__(self, port):
        pValue = 2.3
        iValue = 4
        dValue = 3
        self._portNum = port
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class TempSA(AnalogInput,ControlLoop):
    def __init__(self, port):
        pValue = 2.3
        iValue = 4
        dValue = 3
        self._portNum = port
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class AirFlowOA(AnalogInput,ControlLoop):
    def __init__(self, port):
        pValue = 2.3
        iValue = 4
        dValue = 3
        self._portNum = port
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class AirFlowRA(AnalogInput,ControlLoop):
    def __init__(self, port):
        pValue = 2.3
        iValue = 4
        dValue = 3
        self._portNum = port
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class AirFlowREA(AnalogInput,ControlLoop):
    def __init__(self, port):
        pValue = 2.3
        iValue = 4
        dValue = 3
        self._portNum = port
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class HumidityRA(AnalogInput,ControlLoop):
    def __init__(self, port):
        pValue = 2.3
        iValue = 4
        dValue = 3
        self._portNum = port
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class CORA(AnalogInput,ControlLoop):
    def __init__(self, port):
        pValue = 2.3
        iValue = 4
        dValue = 3
        self._portNum = port
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class TempRA(AnalogInput):
    def __init__(self, port):
        self._portNum = port
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port
        
class TempOA(AnalogInput):
    def __init__(self, port):
        self._portNum = port
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port
	
class HumidityOA(AnalogInput):
    def __init__(self, port):
        self._portNum = port
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class HumidityMA(AnalogInput):
    def __init__(self, port):
        self._portNum = port
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class HumiditySA(AnalogInput):
    def __init__(self, port):
        self._portNum = port
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class AirFlowSA(AnalogInput):
    def __init__(self, port):
        _portNum = port
    def getPortNum():
        return _portNum
    def setPortNum(port):
        _portNum = port

class FilterPDrop(AnalogInput):
    def __init__(self, port):
        self._portNum = port
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class CoolingCoilPDrop(AnalogInput):
    def __init__(self, port):
        self._portNum = port
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class HeatingCoilPDrop(AnalogInput):
    def __init__(self, port):
        self._portNum = port
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class COOA(AnalogInput):
    def __init__(self, port):
        self._portNum = port
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class COMA(AnalogInput):
    def __init__(self, port):
        self._portNum = port
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class COSA(AnalogInput):
    def __init__(self, port):
        self._portNum = port
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class FanVoltage(AnalogInput):
    def __init__(self, port):
        self._portNum = port
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class FanAmperage(AnalogInput):
    def __init__(self, port):
        self._portNum = port
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class FanPower(AnalogInput):
    def __init__(self, port):
        self._portNum = port
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class FanPowerUsage(AnalogInput):
    def __init__(self, port):
        self._portNum = port
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class FanStatus(AnalogInput):
    def __init__(self, port):
        self._portNum = port
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class ChilledWaterST(AnalogInput):
    def __init__(self, port):
        self._portNum = port
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class ChilledWaterRT(AnalogInput):
    def __init__(self, port):
        self._portNum = port
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class ChilledWaterTDrop(AnalogInput):
    def __init__(self, port):
        self._portNum = port
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class ChilledWaterSP(AnalogInput):
    def __init__(self, port):
        self._portNum = port
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class ChilledWaterRP(AnalogInput):
    def __init__(self, port):
        self._portNum = port
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class ChilledWaterPDrop(AnalogInput):
    def __init__(self, port):
        self._portNum = port
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class ChilledWaterFlow(AnalogInput):
    def __init__(self, port):
        self._portNum = port
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class HeatedWaterST(AnalogInput):
    def __init__(self, port):
        self._portNum = port
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class HeatedWaterRT(AnalogInput):
    def __init__(self, port):
        self._portNum = port
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class HeatedWaterTDrop(AnalogInput):
    def __init__(self, port):
        self._portNum = port
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class HeatedWaterSP(AnalogInput):
    def __init__(self, port):
        self._portNum = port
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class HeatedWaterRP(AnalogInput):
    def __init__(self, port):
        self._portNum = port
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class HeatedWaterPDrop(AnalogInput):
    def __init__(self, port):
        self._portNum = port
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class HeatedWaterFlow(AnalogInput):
    def __init__(self, port):
        self._portNum = port
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

#Outputs
#class DamperPositionOA(AnalogOutput):
#class DamperPositionRA(AnalogOutput):
#class DamperPositionRE(AnalogOutput):
#class ValuePositionCW(AnalogOutput):
#class ValuePositionHW(AnalogOutput):
#class valuePositionHumidifier(AnalogOutput):
#class fanSpeedFrequency(AnalogOutput):
#class fanSpeedOutput(AnalogOutput):


#Class for controlling the device parameters

class Device(object):
    def __init__(self, objectName, deviceAddress, objectIdentifier, maxApduLengthAccepted, segmentationSupported, vendorIdentifier, foreignPort, foreignBBMD, foreignTTL, requestAddress):
        self._objectName = objectName
        self._deviceAddress = deviceAddress
        self._requestAddress = requestAddress
        self._objectIdentifier = objectIdentifier
        self._maxApduLengthAccepted = maxApduLengthAccepted
        self._segmentationSupported = segmentationSupported
        self._vendorIdentifier = vendorIdentifier
        self._foreignPort = foreignPort
        self._foreignBBMD = foreignBBMD
        self._foreignTTL = foreignTTL
        self._next = None
        self._online = True
        self._manual = False
        self._KILL = False
        
    def addDevice(self, nextDevice):
        self._next = nextDevice

    def getObjectName(self):   
        return self._objectName
    
    def getDeviceAddress(self):   
        return self._deviceAddress
    
    def getRequestAddress(self):   
        return self._requestAddress
    
    def getObjectIdentifier(self):   
        return self._objectIdentifier
    
    def getMaxApduLengthAccepted(self):   
        return self._maxApduLengthAccepted
    
    def getSegmentationSupported(self):   
        return self._segmentationSupported
    
    def getVendorIdentifier(self):   
        return self._vendorIdentifier
    
    def getForeignPort(self):   
        return self._foreignPort
    
    def getForeignBBMD(self):   
        return self._foreignBBMD
    
    def getForeignTTL(self):   
        return self._foreignTTL
    
    def getNext(self):   
        return self._next
    
    def setObjectName(self, name):   
        self._objectName = name    
    
    def setDeviceAddress(self, addr):   
        self._deviceAddress = addr
    
    def setRequestAddress(self, addr):   
        self._requestAddress = addr
    
    def setObjectIdentifier(self, obj):   
        self._objectIdentifier = obj
    
    def setMaxApduLengthAccepted(self, APDU):   
        self._maxApduLengthAccepted = APDU
    
    def setSegmentationSupported(self, seg):   
        self._segmentationSupported  = seg
    
    def setVendorIdentifier(self, vend):   
        self._vendorIdentifier = vend
    
    def setForeignPort(self, port):   
        self._foreignPort = port
    
    def setForeignBBMD(self, BBMD):   
        self._foreignBBMD = BBMD
    
    def setForeignTTL(self, TTL):   
        self._foreignTTL = TTL
    
    def setNext(self, next):   
        self._next = next


