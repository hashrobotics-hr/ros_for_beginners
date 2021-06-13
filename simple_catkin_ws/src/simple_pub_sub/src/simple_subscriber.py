#!/usr/bin/env python3

import rospy
from std_msgs.msg import String


def Subscriber():
	sub = rospy.Subscriber('/simple_publisher',String,print_result)
	rospy.spin()
	
def print_result(data):
	rospy.loginfo(data)

if __name__ == '__main__':
	rospy.init_node('simple_subscriber_node')
	Subscriber()
