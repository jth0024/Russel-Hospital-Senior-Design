import ConfigParser
Config = ConfigParser.ConfigParser()

def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

def requestIPToCompIP(requestIP):
	IPAddress = requestIP[-2:]
	IPAddress = int(IPAddress) - int(1)
	IPAddress = str(requestIP)[:-2] + str(IPAddress)
	return IPAddress

def iniParser(iniFile):
    Config.read(iniFile)
    Name = ConfigSectionMap("BACpypes")['objectname']
    print 'The name of the device is ' + Name
    requestAddress = ConfigSectionMap("BACpypes")['address']
    compIP = requestIPToCompIP(requestAddress)
    print 'The request IP Address is: ' + requestAddress
    print 'The computer IP Address is: ' + compIP