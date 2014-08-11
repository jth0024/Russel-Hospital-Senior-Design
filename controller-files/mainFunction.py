from fileToDic import fileToDic
from DeviceRead import deviceRead

deviceDic = fileToDic('DeviceList.txt')
#print deviceDic
valDic = deviceRead(deviceDic)
print valDic
#print valDic["192.168.92.68"][1]
