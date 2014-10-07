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

def CompIPToRequestIP(compIP):
	RequestIP = compIP[-2:]
	RequestIP = int(RequestIP) - int(1)
	RequestIP = str(compIP)[:-2] + str(RequestIP)
	return RequestIP

def iniParser(iniFile):
    Config.read(iniFile)
    dictionary = ConfigSectionMap("BACpypes")
    return dictionary.values()

