from createDeviceChain import createChain


devices = createChain()

print devices.getPortItem(2).getPortNum()
