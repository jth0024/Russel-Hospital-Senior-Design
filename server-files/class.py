class AnalogInput(object):
	type = 'analogInput'
	value = 'presentValue'
class AnalogOutput(object):
	type = 'analogOutput'
	value = 'presentValue'
	index = 0
	priority = 1
class DigitalInput(object):
	type = 'digitalInput'
	value = 'presentValue'
class DigitalOutput(object):
	type = 'digitalOutput'
	value = 'presentValue'
	index = 0
	priority = 1	
class RATemp(AnalogInput):
	pValue = 2.3
	iValue = 4
	Dvalue = 3
	def Ploop(setpoint,currentValue,pValue):
		outputValue = pValue*(setpoint-currentValue)
		return outputValue
	def PIloop(setpoint,currentValue,pValue,iValue):
		outputValue = 'Insert control eqation here'
		return outputValue
	def PIDloop(setpoint,currentValue,pValue,iValue,dValue):
		outputValue = 'Insert control eqation here'
		return outputValue

