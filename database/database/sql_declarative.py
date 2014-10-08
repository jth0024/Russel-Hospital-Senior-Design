import os
import sys
import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Date, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Devices(Base):
	__tablename__ = 'devices'
	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	ini = Column(String(250), nullable=False)
	ip = Column(String(250), nullable=False)
	mac = Column(String(250), nullable=False)
	

class Errors(Base):
	__tablename__= 'errors'
	id = Column(Float, primary_key=True)
	type = Column(String(250), nullable=False)
	timestamp = Column(DateTime, default=datetime.datetime.utcnow)
	priority = Column(Float)
	location = Column(String(250))
	device = Column(String(250), nullable=False)

class Maintenance(Base):
	__tablename__ = 'maintenance'
	id = Column(Float, primary_key=True)
	timestamp = Column(DateTime, default=datetime.datetime.utcnow)
	dueDate = Column(Date, nullable=False)
	priority = Column(Float)
	description = Column(String(250), nullable=False)

class AirHandlerOne(Base):
	__tablename__ = 'airhandlerOne'
	id = Column(Integer, primary_key=True)
	timestamp = Column(DateTime, default=datetime.datetime.utcnow)
	tempOA = Column(Float)
	tempRA = Column(Float)
	tempMA = Column(Float)
	tempPA = Column(Float)
	tempSA = Column(Float)
	humidityOA = Column(Float)
	humidityRA = Column(Float)
	humiditySA = Column(Float)
	airFlowOA = Column(Float)
	airFlowRA = Column(Float)
	airFlowREA = Column(Float)
	airFlowSA = Column(Float)
	filterPDrop = Column(Float)
	coolingCoilPDrop = Column(Float)
	heatingCoilPDrop = Column(Float)
	coOA = Column(Float)
	coRA = Column(Float)
	coMA = Column(Float)
	coSA = Column(Float)
	fanVoltage = Column(Float)
	fanAmperage = Column(Float)
	fanPower = Column(Float)
	fanPowerUsage = Column(Float)
	fanStatus = Column(Boolean)
	chilledWaterST = Column(Float)
	chilledWaterRT = Column(Float)
	chilledWaterTDrop = Column(Float)
	chilledWaterSP = Column(Float)
	chilledWaterRP = Column(Float)
	chilledWaterPDrop = Column(Float)
	chilledWaterFlow = Column(Float)
	heatedWaterST = Column(Float)
	heatedWaterRT = Column(Float)
	heatedWaterTDrop = Column(Float)
	heatedWaterSP = Column(Float)
	heatedWaterRP = Column(Float)
	heatedaterPDrop = Column(Float)
	heatedWaterFlow = Column(Float)
	damperPositionOA = Column(Float)
	damperPositionRA = Column(Float)
	damperPositionRE = Column(Float)
	valuePositionCW = Column(Float)
	valuePositionHW = Column(Float)
	valuePositionHumidifier = Column(Float)
	fanSpeedFrequency = Column(Float)
	fanSpeedOutput = Column(Float)

class Setpoints(Base):
	__tablename__ = 'setpoint'
	id = Column(Integer, primary_key=True)
	timestamp = Column(DateTime, default=datetime.datetime.utcnow)
	tempSA = Column(Float)
	tempPA = Column(Float)
	tempMA = Column(Float)
	humidityRA = Column(Float)
	pressureDischargeStatic	 = Column(Float)
	airFlowOA = Column(Float)
	airFlowRA = Column(Float)
	airFlowReliefA = Column(Float)
	coRA = Column(Float)




# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///rh.db')
# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)

