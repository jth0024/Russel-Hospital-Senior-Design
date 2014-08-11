'''Builds a read request using Bacnet IP and sends request to the device
This is just a demo program and needs to be changed to send the request'''

#from bacpypes.object import get_object_class
from bacpypes.apdu import ReadPropertyRequest, ReadPropertyACK
from bacpypes.pdu import Address
from bacpypes.app import BIPSimpleApplication, LocalDeviceObject
#from bacpypes.consolelogging import ConfigArgumentParser
#from bacpypes.basetypes import ServicesSupported
from bacpypes.object import get_datatype


class ReadPropertyApplication(BIPSimpleApplication):

    def __init__(self, *args):
#        if _debug: ReadPropertyApplication._debug("__init__ %r", args)
        BIPSimpleApplication.__init__(self, *args)

        # keep track of requests to line up responses
        self._request = None

    def request(self, apdu):
#        if _debug: ReadPropertyApplication._debug("request %r", apdu)

        # save a copy of the request
        self._request = apdu

        # forward it along
        BIPSimpleApplication.request(self, apdu)

    def confirmation(self, apdu):
#        if _debug: ReadPropertyApplication._debug("confirmation %r", apdu)

#        if isinstance(apdu, Error):
#           sys.stdout.write("error: %s\n" % (apdu.errorCode,))
#            sys.stdout.flush()

#        elif isinstance(apdu, AbortPDU):
#            apdu.debug_contents()

#        if isinstance(apdu, SimpleAckPDU):
#            sys.stdout.write("ack\n")
#            sys.stdout.flush()

        if (isinstance(self._request, ReadPropertyRequest)) and (isinstance(apdu, ReadPropertyACK)):
            # find the datatype
            datatype = get_datatype(apdu.objectIdentifier[0], apdu.propertyIdentifier)
#            if _debug: ReadPropertyApplication._debug("    - datatype: %r", datatype)
            if not datatype:
                raise TypeError, "unknown datatype"
#
#            # special case for array parts, others are managed by cast_out
#            if issubclass(datatype, Array) and (apdu.propertyArrayIndex is not None):
#                if apdu.propertyArrayIndex == 0:
#                    value = apdu.propertyValue.cast_out(Unsigned)
#                else:
#                    value = apdu.propertyValue.cast_out(datatype.subtype)
            else:
                value = apdu.propertyValue.cast_out(datatype)
#            if _debug: ReadPropertyApplication._debug("    - value: %r", value)

            return value  

#            sys.stdout.write(str(value) + '\n')
#            sys.stdout.flush()





def readRequest(str_ipAddress, int_port):
      # parse the command line arguments
#    args = ConfigArgumentParser(description=__doc__).parse_args()
     
     # make a device object
    this_device = LocalDeviceObject(
        objectName= str_ipAddress,#args.ini.objectname,
        objectIdentifier= 2450, #int(args.ini.objectidentifier),
        maxApduLengthAccepted= 1024, #int(args.ini.maxapdulengthaccepted),
        segmentationSupported="segmentedBoth", #args.ini.segmentationsupported,
        vendorIdentifier=25, #int(args.ini.vendoridentifier),
        )

    # build a bit string that knows about the bit names
#    pss = ServicesSupported()
#    pss['whoIs'] = 1
#    pss['iAm'] = 1
#    pss['readProperty'] = 1
#    pss['writeProperty'] = 1

    # set the property value to be just the bits
#    this_device.protocolServicesSupported = pss.value
    
    if str_ipAddress == "192.168.92.68":
        addr = str_ipAddress
        obj_type = "analogInp1ut"
        prop_id = "presentValue"
        port = int(int_port)
        this_application = ReadPropertyApplication(this_device, addr)
    #    if obj_type.isdigit():
    #        obj_type = int(obj_type)
    #    elif not get_object_class(obj_type):
    #        raise ValueError, "unknown object type"
   
    #    datatype = get_datatype(obj_type, prop_id)
    #    if not datatype:
    #        raise ValueError, "invalid property for object type"
    
        request = ReadPropertyRequest( objectIdentifier=(obj_type, port),
            propertyIdentifier=prop_id)
        request.pduDestination = Address(addr)
        this_application.request(request)   
    
    
    if str_ipAddress == "192.168.92.50":
       # print "50"
        return 50
    else:
        #print "25"
        return 25
