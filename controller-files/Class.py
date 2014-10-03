
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

#Inputs
#class TempRA(AnalogInput):
#class TempOA(AnalogInput):
class TempMA(AnalogInput,ControlLoop):
	pValue = 2.3
	iValue = 4
	Dvalue = 3
class TempPA(AnalogInput,ControlLoop):
	pValue = 2.3
	iValue = 4
	Dvalue = 3
class TempSA(AnalogInput,ControlLoop):
	pValue = 2.3
	iValue = 4
	Dvalue = 3
#class HumidityOA(AnalogInput):
class HumidityRA(AnalogInput,ControlLoop):
	pValue = 2.3
	iValue = 4
	Dvalue = 3
#class HumidityMA(AnalogInput):
#class HumiditySA(AnalogInput):
class AirFlowOA(AnalogInput,ControlLoop):
	pValue = 2.3
	iValue = 4
	Dvalue = 3
class AirFlowRA(AnalogInput,ControlLoop):
	pValue = 2.3
	iValue = 4
	Dvalue = 3
class AirFlowREA(AnalogInput,ControlLoop):
	pValue = 2.3
	iValue = 4
	Dvalue = 3
#class AirFlowSA(AnalogInput):
#class FilterPDrop(AnalogInput):
#class CoolingCoilPDrop(AnalogInput):
#class HeatingCoilPDrop(AnalogInput):
#class COOA(AnalogInput):
class CORA(AnalogInput,ControlLoop):
	pValue = 2.3
	iValue = 4
	Dvalue = 3
#class COMA(AnalogInput):
#class COSA(AnalogInput):
#class FanVoltage(AnalogInput):
#class FanAmperage(AnalogInput):
#class FanPower(AnalogInput):
#class FanPowerUsage(AnalogInput):
#class FanStatus(AnalogInput):
#class ChilledWaterST(AnalogInput):
#class ChilledWaterRT(AnalogInput):
#class ChilledWaterTDrop(AnalogInput):
#class ChilledWaterSP(AnalogInput):
#class ChilledWaterRP(AnalogInput):
#class ChilledWaterPDrop(AnalogInput):
#class ChilledWaterFlow(AnalogInput):
#class HeatedWaterST(AnalogInput):
#class HeatedWaterRT(AnalogInput):
#class HeatedWaterTDrop(AnalogInput):
#class HeatedWaterSP(AnalogInput):
#class HeatedWaterRP(AnalogInput):
#class HeatedWaterPDrop(AnalogInput):
#class HeatedWaterFlow(AnalogInput):

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


