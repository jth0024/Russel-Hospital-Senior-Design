class AnalogInput(object):
	
	def __init__(self):
	    self._type = 'analogInput'
	    self._prop = 'presentValue'
	def getType(self):
		return self._type
	def getProp(self):
		return self._prop
	def setType(self,type):
		self._type = type
	def setValue(self,value):
		self._value = value	


class AnalogOutput(object):
	
	def __init__(self):
	    self._type = 'analogOutput'
	    self._prop = 'presentValue'
	    self._index = 0
	    self._priority = 1
	def getType(self):
		return self._type
	def getProp(self):
		return self._prop
	def getIndex(self):
		return self._index
	def getPriority(self):
		return self._priority
	def setType(self,Type):
		self._type = Type
	def setValue(self,value):
		self._value = value
	def setIndex(self, index):
		self._index = index
	def setPriority(self, priority):
		self._priority = priority

class DigitalInput(object):
	
	def __init__(self):
	    self._type = 'digitalInput'
	    self._value = 'presentValue'

	def gettype(self):
		return self.type
	def getvalue(self):
		return self.value
	def settype(self,type):
		self.type = type
	def setValue(self,value):
		self.value = value	


class DigitalOutput(object):
	def __init__(self):
	    self._type = 'digitalOutput'
	    self._value = 'presentValue'
	    self._index = 0
	    self._priority = 1

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
	def __init__(self):
        self._connectedTo = 1
	    return
    
	def Ploop(self, setpoint,currentValue):
		outputValue = self._pValue*(setpoint-currentValue)
		return outputValue
	def PIloop(self, setpoint,currentValue,pValue,iValue):
		outputValue = 'Insert control eqation here'
		return outputValue
	def PIDloop(self, setpoint,currentValue,pValue,iValue,dValue):
		outputValue = 'Insert control eqation here'
		return outputValue
    def getConnectedTo():
        return self._connectedTo

### Inputs
#add name field

class TempMA(AnalogInput,ControlLoop):
    
    def __init__(self, port):
        AnalogInput.__init__(self)
        ControlLoop.__init__(self)
        self._portNum = port
        self._pValue = 2.3
        self._iValue = 4
        self._dValue = 3
        self._controlled = True
    def getControlled(self):
        return self._controlled
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port
    def getPValue(self):
        return self._pValue
    def setPValue(self, pValue):
        self._pValue = pValue
    def getIValue(self):
        return self._iValue
    def setIValue(self, iValue):
        self._iValue = iValue
    def getDValue(self):
        return self._dValue
    def setDValue(self, dValue):
        self._dValue = dValue

class TempPA(AnalogInput,ControlLoop):
    def __init__(self, port):
        AnalogInput.__init__(self)
        ControlLoop.__init__(self)
        self._portNum = port
        self._pValue = 2.3
        self._iValue = 4
        self._dValue = 3
        self._controlled = True
    def getControlled(self):
        return self._controlled
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port
    def getPValue(self):
        return self._pValue
    def setPValue(self, pValue):
        self._pValue = pValue
    def getIValue(self):
        return self._iValue
    def setIValue(self, iValue):
        self._iValue = iValue
    def getDValue(self):
        return self._dValue
    def setDValue(self, dValue):
        self._dValue = dValue        

class TempSA(AnalogInput,ControlLoop):
    def __init__(self, port):
        AnalogInput.__init__(self)
        ControlLoop.__init__(self)
        self._portNum = port
        self._pValue = 2.3
        self._iValue = 4
        self._dValue = 3
        self._controlled = True
    def getControlled(self):
        return self._controlled
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port
    def getPValue(self):
        return self._pValue
    def setPValue(self, pValue):
        self._pValue = pValue
    def getIValue(self):
        return self._iValue
    def setIValue(self, iValue):
        self._iValue = iValue
    def getDValue(self):
        return self._dValue
    def setDValue(self, dValue):
        self._dValue = dValue
        
        
class AirFlowOA(AnalogInput,ControlLoop):
    def __init__(self, port):
        AnalogInput.__init__(self)
        ControlLoop.__init__(self)
        self._portNum = port
        self._pValue = 2.3
        self._iValue = 4
        self._dValue = 3
        self._controlled = True
    def getControlled(self):
        return self._controlled
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port
    def getPValue(self):
        return self._pValue
    def setPValue(self, pValue):
        self._pValue = pValue
    def getIValue(self):
        return self._iValue
    def setIValue(self, iValue):
        self._iValue = iValue
    def getDValue(self):
        return self._dValue
    def setDValue(self, dValue):
        self._dValue = dValue
        
        
class AirFlowRA(AnalogInput,ControlLoop):
    def __init__(self, port):
        AnalogInput.__init__(self)
        ControlLoop.__init__(self)
        self._portNum = port
        self._pValue = 2.3
        self._iValue = 4
        self._dValue = 3
        self._controlled = True
    def getControlled(self):
        return self._controlled
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port
    def getPValue(self):
        return self._pValue
    def setPValue(self, pValue):
        self._pValue = pValue
    def getIValue(self):
        return self._iValue
    def setIValue(self, iValue):
        self._iValue = iValue
    def getDValue(self):
        return self._dValue
    def setDValue(self, dValue):
        self._dValue = dValue
        
        
class AirFlowREA(AnalogInput,ControlLoop):
    def __init__(self, port):
        AnalogInput.__init__(self)
        ControlLoop.__init__(self)
        self._portNum = port
        self._pValue = 2.3
        self._iValue = 4
        self._dValue = 3
        self._controlled = True
    def getControlled(self):
        return self._controlled
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port
    def getPValue(self):
        return self._pValue
    def setPValue(self, pValue):
        self._pValue = pValue
    def getIValue(self):
        return self._iValue
    def setIValue(self, iValue):
        self._iValue = iValue
    def getDValue(self):
        return self._dValue
    def setDValue(self, dValue):
        self._dValue = dValue
        
        
class HumidityRA(AnalogInput,ControlLoop):
    def __init__(self, port):
        AnalogInput.__init__(self)
        ControlLoop.__init__(self)
        self._portNum = port
        self._pValue = 2.3
        self._iValue = 4
        self._dValue = 3
        self._controlled = True
    def getControlled(self):
        return self._controlled
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port
    def getPValue(self):
        return self._pValue
    def setPValue(self, pValue):
        self._pValue = pValue
    def getIValue(self):
        return self._iValue
    def setIValue(self, iValue):
        self._iValue = iValue
    def getDValue(self):
        return self._dValue
    def setDValue(self, dValue):
        self._dValue = dValue
        
        
class CORA(AnalogInput,ControlLoop):
    def __init__(self, port):
        AnalogInput.__init__(self)
        ControlLoop.__init__(self)
        self._portNum = port
        self._pValue = 2.3
        self._iValue = 4
        self._dValue = 3
        self._controlled = True
    def getControlled(self):
        return self._controlled
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port
    def getPValue(self):
        return self._pValue
    def setPValue(self, pValue):
        self._pValue = pValue
    def getIValue(self):
        return self._iValue
    def setIValue(self, iValue):
        self._iValue = iValue
    def getDValue(self):
        return self._dValue
    def setDValue(self, dValue):
        self._dValue = dValue
        
        
class TempRA(AnalogInput):
    def __init__(self, port):
        AnalogInput.__init__(self)
        self._portNum = port
        self._controlled = False
    def getControlled(self):
        return self._controlled
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port
        
class TempOA(AnalogInput):
    def __init__(self, port):
        AnalogInput.__init__(self)
        self._portNum = port
        self._controlled = False
    def getControlled(self):
        return self._controlled
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port
	
class HumidityOA(AnalogInput):
    def __init__(self, port):
        AnalogInput.__init__(self)
        self._portNum = port
        self._controlled = False
    def getControlled(self):
        return self._controlled
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class HumidityMA(AnalogInput):
    def __init__(self, port):
        AnalogInput.__init__(self)
        self._portNum = port
        self._controlled = False
    def getControlled(self):
        return self._controlled
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class HumiditySA(AnalogInput):
    def __init__(self, port):
        AnalogInput.__init__(self)
        self._portNum = port
        self._controlled = False
    def getControlled(self):
        return self._controlled
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class AirFlowSA(AnalogInput):
    def __init__(self, port):
        AnalogInput.__init__(self)
        self._portNum = port
        self._controlled = False
    def getControlled(self):
        return self._controlled
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class FilterPDrop(AnalogInput):
    def __init__(self, port):
        AnalogInput.__init__(self)
        self._portNum = port
        self._controlled = False
    def getControlled(self):
        return self._controlled
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class CoolingCoilPDrop(AnalogInput):
    def __init__(self, port):
        AnalogInput.__init__(self)
        self._portNum = port
        self._controlled = False
    def getControlled(self):
        return self._controlled
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class HeatingCoilPDrop(AnalogInput):
    def __init__(self, port):
        AnalogInput.__init__(self)
        self._portNum = port
        self._controlled = False
    def getControlled(self):
        return self._controlled
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class COOA(AnalogInput):
    def __init__(self, port):
        AnalogInput.__init__(self)
        self._portNum = port
        self._controlled = False
    def getControlled(self):
        return self._controlled
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class COMA(AnalogInput):
    def __init__(self, port):
        AnalogInput.__init__(self)
        self._portNum = port
        self._controlled = False
    def getControlled(self):
        return self._controlled
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class COSA(AnalogInput):
    def __init__(self, port):
        AnalogInput.__init__(self)
        self._portNum = port
        self._controlled = False
    def getControlled(self):
        return self._controlled
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class FanVoltage(AnalogInput):
    def __init__(self, port):
        AnalogInput.__init__(self)
        self._portNum = port
        self._controlled = False
    def getControlled(self):
        return self._controlled
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class FanAmperage(AnalogInput):
    def __init__(self, port):
        AnalogInput.__init__(self)
        self._portNum = port
        self._controlled = False
    def getControlled(self):
        return self._controlled
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class FanPower(AnalogInput):
    def __init__(self, port):
        AnalogInput.__init__(self)
        self._portNum = port
        self._controlled = False
    def getControlled(self):
        return self._controlled
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class FanPowerUsage(AnalogInput):
    def __init__(self, port):
        AnalogInput.__init__(self)
        self._portNum = port
        self._controlled = False
    def getControlled(self):
        return self._controlled
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class FanStatus(AnalogInput):
    def __init__(self, port):
        AnalogInput.__init__(self)
        self._portNum = port
        self._controlled = False
    def getControlled(self):
        return self._controlled
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class ChilledWaterST(AnalogInput):
    def __init__(self, port):
        AnalogInput.__init__(self)
        self._portNum = port
        self._controlled = False
    def getControlled(self):
        return self._controlled
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class ChilledWaterRT(AnalogInput):
    def __init__(self, port):
        AnalogInput.__init__(self)
        self._portNum = port
        self._controlled = False
    def getControlled(self):
        return self._controlled
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class ChilledWaterTDrop(AnalogInput):
    def __init__(self, port):
        AnalogInput.__init__(self)
        self._portNum = port
        self._controlled = False
    def getControlled(self):
        return self._controlled
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class ChilledWaterSP(AnalogInput):
    def __init__(self, port):
        AnalogInput.__init__(self)
        self._portNum = port
        self._controlled = False
    def getControlled(self):
        return self._controlled
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class ChilledWaterRP(AnalogInput):
    def __init__(self, port):
        AnalogInput.__init__(self)
        self._portNum = port
        self._controlled = False
    def getControlled(self):
        return self._controlled
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class ChilledWaterPDrop(AnalogInput):
    def __init__(self, port):
        AnalogInput.__init__(self)
        self._portNum = port
        self._controlled = False
    def getControlled(self):
        return self._controlled
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class ChilledWaterFlow(AnalogInput):
    def __init__(self, port):
        AnalogInput.__init__(self)
        self._portNum = port
        self._controlled = False
    def getControlled(self):
        return self._controlled
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class HeatedWaterST(AnalogInput):
    def __init__(self, port):
        AnalogInput.__init__(self)
        self._portNum = port
        self._controlled = False
    def getControlled(self):
        return self._controlled
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class HeatedWaterRT(AnalogInput):
    def __init__(self, port):
        AnalogInput.__init__(self)
        self._portNum = port
        self._controlled = False
    def getControlled(self):
        return self._controlled
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class HeatedWaterTDrop(AnalogInput):
    def __init__(self, port):
        AnalogInput.__init__(self)
        self._portNum = port
        self._controlled = False
    def getControlled(self):
        return self._controlled
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class HeatedWaterSP(AnalogInput):
    def __init__(self, port):
        AnalogInput.__init__(self)
        self._portNum = port
        self._controlled = False
    def getControlled(self):
        return self._controlled
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class HeatedWaterRP(AnalogInput):
    def __init__(self, port):
        AnalogInput.__init__(self)
        self._portNum = port
        self._controlled = False
    def getControlled(self):
        return self._controlled
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class HeatedWaterPDrop(AnalogInput):
    def __init__(self, port):
        AnalogInput.__init__(self)
        self._portNum = port
        self._controlled = False
    def getControlled(self):
        return self._controlled
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

class HeatedWaterFlow(AnalogInput):
    def __init__(self, port):
        AnalogInput.__init__(self)
        self._portNum = port
        self._controlled = False
    def getControlled(self):
        return self._controlled
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

#Outputs
class DamperPositionOA(AnalogOutput):
    def __init__(self, port):
        AnalogOutput.__init__(self)
        self._portNum = port
        self._controlled = False
    def getControlled(self):
        return self._controlled
    def getPortNum(self):
        return self._portNum
    def setPortNum(self, port):
        self._portNum = port

#class DamperPositionRA(AnalogOutput):
#class DamperPositionRE(AnalogOutput):
#class ValuePositionCW(AnalogOutput):
#class ValuePositionHW(AnalogOutput):
#class valuePositionHumidifier(AnalogOutput):
#class fanSpeedFrequency(AnalogOutput):
#class fanSpeedOutput(AnalogOutput):


#Class for controlling the device parameters
#deviceDic['objectname'],deviceDic['address'],
#            deviceDic['objectidentifier'],deviceDic['maxapdulengthaccepted'],
#            deviceDic['segmentationsupported'],deviceDic['vendoridentifier'],
#            deviceDic['foreignport'],deviceDic['foreignbbmd'],
#            deviceDic['foreignttl'],deviceDic['requestip']



class Device(object):
    def __init__(self, deviceDic, portDic):
        self._objectName = deviceDic['objectname']
        self._deviceAddress = deviceDic['address']
        self._requestAddress = deviceDic['requestip']
        self._objectIdentifier = deviceDic['objectidentifier']
        self._maxApduLengthAccepted = deviceDic['maxapdulengthaccepted']
        self._segmentationSupported = deviceDic['segmentationsupported']
        self._vendorIdentifier = deviceDic['vendoridentifier']
        self._foreignPort = deviceDic['foreignport']
        self._foreignBBMD = deviceDic['foreignbbmd']
        self._foreignTTL = deviceDic['foreignttl']       
        self._ports = portDic
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
    
    def getPort(self):
        return self._ports
    
    def getPortItem(self, portNumber):
        if portNumber == 1:
            return self._ports["portone"]
        elif portNumber == 2:
            return self._ports["porttwo"]
        elif portNumber == 3:
            return self._ports["portthree"]
        elif portNumber == 4:
            return self._ports["portfour"]
        elif portNumber == 5:
            return self._ports["portfive"]
        elif portNumber == 6:
            return self._ports["portsix"]
        elif portNumber == 7:
            return self._ports["portseven"]
        else:
            return "Error: Port unknown"
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



