#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import RPi.GPIO as GPIO
import time

ir_sensor = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(ir_sensor,GPIO.IN)


def Publisher():
	pub =  rospy.Publisher('/simple_publisher',String,queue_size=10)
	rate = rospy.Rate(1)
	message = String()
	while not rospy.is_shutdown():
		if GPIO.input(ir_sensor)==1:
			message.data="Object Not Detected"
		else:
			message.data="Object Detected"
		pub.publish(message)
		rate.sleep()
		
	rospy.loginfo("Node Stopped")
		
	

if __name__ == '__main__':
	rospy.init_node('simple_publisher_node')
	Publisher()
