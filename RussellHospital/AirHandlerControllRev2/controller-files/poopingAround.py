manipulatedDic = {}
manipulatedDic[1] = None
manipulatedDic[2] = -0.63
manipulatedDic[3] = 2.5
manipulatedDic[4] = 10.0

print manipulatedDic
for value in manipulatedDic:
    if manipulatedDic[value] != None:
        if manipulatedDic[value] < 0:
            manipulatedDic[value] = 0.0
        elif manipulatedDic[value] > 4:
            manipulatedDic[value] = 4.0
print "things: " + str(manipulatedDic)
