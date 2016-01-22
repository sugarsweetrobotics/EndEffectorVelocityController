#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file EndEffectorVelocityController.py
 @brief Control Manipulator with 3 dimension velocity
 @date $Date$


"""
import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist

import ManipulatorCommonInterface_MiddleLevel_idl

# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
import JARA_ARM, JARA_ARM__POA


# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
endeffectorvelocitycontroller_spec = ["implementation_id", "EndEffectorVelocityController", 
		 "type_name",         "EndEffectorVelocityController", 
		 "description",       "Control Manipulator with 3 dimension velocity", 
		 "version",           "1.0.0", 
		 "vendor",            "Sugar Sweet Robotics", 
		 "category",          "Manipulator", 
		 "activity_type",     "STATIC", 
		 "max_instance",      "1", 
		 "language",          "Python", 
		 "lang_type",         "SCRIPT",
		 "conf.default.debug", "0",
		 "conf.__widget__.debug", "text",
		 ""]
# </rtc-template>

##
# @class EndEffectorVelocityController
# @brief Control Manipulator with 3 dimension velocity
# 
# 
class EndEffectorVelocityController(OpenRTM_aist.DataFlowComponentBase):
	
	##
	# @brief constructor
	# @param manager Maneger Object
	# 
	def __init__(self, manager):
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

		self._d_velocity = RTC.TimedVelocity3D(RTC.Time(0,0),RTC.Velocity3D(0,0,0,0,0,0))
		"""
		"""
		self._velocityIn = OpenRTM_aist.InPort("velocity", self._d_velocity)
		self._d_currentPosition = RTC.TimedPose3D(RTC.Time(0,0),RTC.Pose3D(RTC.Point3D(0,0,0),RTC.Orientation3D(0,0,0)))
		"""
		"""
		self._currentPositionOut = OpenRTM_aist.OutPort("currentPosition", self._d_currentPosition)

		"""
		"""
		self._manipMiddlePort = OpenRTM_aist.CorbaPort("manipMiddle")

		

		"""
		"""
		self._manipMiddle = OpenRTM_aist.CorbaConsumer(interfaceType=JARA_ARM.ManipulatorCommonInterface_Middle)

		# initialize of configuration-data.
		# <rtc-template block="init_conf_param">
		"""
		
		 - Name:  debug
		 - DefaultValue: 0
		"""
		self._debug = [0]
		
		# </rtc-template>


		 
	##
	#
	# The initialize action (on CREATED->ALIVE transition)
	# formaer rtc_init_entry() 
	# 
	# @return RTC::ReturnCode_t
	# 
	#
	def onInitialize(self):
		# Bind variables and configuration variable
		self.bindParameter("debug", self._debug, "0")
		
		# Set InPort buffers
		self.addInPort("velocity",self._velocityIn)
		
		# Set OutPort buffers
		self.addOutPort("currentPosition",self._currentPositionOut)
		
		# Set service provider to Ports
		
		# Set service consumers to Ports
		self._manipMiddlePort.registerConsumer("JARA_ARM_ManipulatorCommonInterface_Middle", "JARA_ARM::ManipulatorCommonInterface_Middle", self._manipMiddle)
		
		# Set CORBA Service Ports
		self.addPort(self._manipMiddlePort)
		
		return RTC.RTC_OK
	
	#	##
	#	# 
	#	# The finalize action (on ALIVE->END transition)
	#	# formaer rtc_exiting_entry()
	#	# 
	#	# @return RTC::ReturnCode_t
	#
	#	# 
	#def onFinalize(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The startup action when ExecutionContext startup
	#	# former rtc_starting_entry()
	#	# 
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onStartup(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The shutdown action when ExecutionContext stop
	#	# former rtc_stopping_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onShutdown(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The activated action (Active state entry action)
	#	# former rtc_active_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	# 
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	def onActivated(self, ec_id):
                while not self._velocityIn.isNew():
                        print '[RTC.EndEffectorVelocityController] Waiting for the First Velocity data.'
                
		self._d_velocity = self._velocityIn.read()
                print '[RTC.EndEffectorVelocityController] Velocity = ', self._d_velocity
		return RTC.RTC_OK
	
	#	##
	#	#
	#	# The deactivated action (Active state exit action)
	#	# former rtc_active_exit()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onDeactivated(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The execution action that is invoked periodically
	#	# former rtc_active_do()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	def onExecute(self, ec_id):
		if self._velocityIn.isNew():
			tk0 = self._d_velocity.tm.sec + self._d_velocity.tm.nsec / 1000000000.0 
			vx= self._d_velocity.data.vx
			vy= self._d_velocity.data.vy
			vz= self._d_velocity.data.vz
			wr= self._d_velocity.data.vr
			wp= self._d_velocity.data.vp
			wy= self._d_velocity.data.va

			self._d_velocity = self._velocityIn.read()
                        print '[RTC.EndEffectorVelocityController] Velocity = ', self._d_velocity
			tk1 = self._d_velocity.tm.sec + self._d_velocity.tm.nsec / 1000000000.0 
			dt = tk1 - tk0
                        print '[RTC.EndEffectorVelocityController] Delta Time = ', dt
			
			dx = vx * dt
			dy = vy * dt
			dz = vz * dt
			droll = wr * dt
			dpitch = wp * dt
			dyaw = wy * dt
			carPoint = JARA_ARM.CarPosWithElbow([[1,0,0,dx],[0,1,0,dy],[0,0,1,dz]], 0.0, 0)
			print '[RTC.EndEffectorVelocityController] Calling movePTPCartesianRel with ', carPoint
			self._manipMiddle._ptr().movePTPCartesianRel(carPoint)
			
		return RTC.RTC_OK
	
	#	##
	#	#
	#	# The aborting action when main logic error occurred.
	#	# former rtc_aborting_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onAborting(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The error action in ERROR state
	#	# former rtc_error_do()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onError(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The reset action that is invoked resetting
	#	# This is same but different the former rtc_init_entry()
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onReset(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The state update action that is invoked after onExecute() action
	#	# no corresponding operation exists in OpenRTm-aist-0.2.0
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#

	#	#
	#def onStateUpdate(self, ec_id):
	#
	#	return RTC.RTC_OK
	
	#	##
	#	#
	#	# The action that is invoked when execution context's rate is changed
	#	# no corresponding operation exists in OpenRTm-aist-0.2.0
	#	#
	#	# @param ec_id target ExecutionContext Id
	#	#
	#	# @return RTC::ReturnCode_t
	#	#
	#	#
	#def onRateChanged(self, ec_id):
	#
	#	return RTC.RTC_OK
	



def EndEffectorVelocityControllerInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=endeffectorvelocitycontroller_spec)
    manager.registerFactory(profile,
                            EndEffectorVelocityController,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    EndEffectorVelocityControllerInit(manager)

    # Create a component
    comp = manager.createComponent("EndEffectorVelocityController")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager()

if __name__ == "__main__":
	main()

