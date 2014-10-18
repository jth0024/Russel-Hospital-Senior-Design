from iniParser import parsePorts

helps = parsePorts("iniFiles/ControllerOne.ini")
help = parsePorts("iniFiles/ControllerFour.ini")

print help
print helps
print len(help)

for item in range(1,len(help)+1):
    print help.getPortItem(item)

