from cplReadWrite2 import read, write, pleaseStop
import time

obj_type = 'analogInput'
obj_inst = int(2)
prop_id = 'presentValue'
ini_name = 'poop'

#start(ini_name)

confirmationValue = read(obj_type, obj_inst, prop_id, ini_name)
print "Current Temperature: " + str(confirmationValue) + "\n"


obj_type = 'analogOutput'
obj_inst = int(3)
value = float(2)
index = int(0)
priority = int(1)

time.sleep(1)

confirmationValue = write(obj_type, obj_inst, prop_id, value, index, priority, ini_name)
print "Write: " + str(confirmationValue)

value = float(0)

time.sleep(10)
print "Lighting LED for 10 seconds"
confirmationValue = write(obj_type, obj_inst, prop_id, value, index, priority, ini_name)
print "Write: " + str(confirmationValue)

pleaseStop()