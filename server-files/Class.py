

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
