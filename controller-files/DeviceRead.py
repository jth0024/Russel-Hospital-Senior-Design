'''Build a read request to read the inputs from each device

need to have the device configured for all inputs then all outputs'''
from ReadRequest import readRequest

def deviceRead(dic_deciveDic):
    input = {}          #create the outer dictionary layer
    maxInput = 2        #max number of I/O ports read by program
    for key in dic_deciveDic:       #This will loop through each of the devices connected to the program
        dictionary = {}         #create the inner dictionary that stores the input readings
        index =1 
        while index <= maxInput:
            dictionary[index] = readRequest(dic_deciveDic[key],index)       #Calls readRequest and gets the value from sensor, loops for each I/O port
            index = index+1
        input[dic_deciveDic[key]] = dictionary          #stores the dictionary of device readings as the element in the outer dictionary, IP address is the key
        del(dictionary)
    return input
