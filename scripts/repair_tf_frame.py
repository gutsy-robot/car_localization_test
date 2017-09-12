#!/usr/bin/env python

import rospy
from sensor_msgs.msg import NavSatFix


class FrameRepair(object):
	def __init__(self):

		rospy.loginfo("Initialising objects for tf frame repair..")
		self.tf_sub = rospy.Subscriber('/fix', NavSatFix, self.tf_cb, queue_size=1)
		self.last_tf = None
		self.tf_pub = rospy.Publisher('/fix_new', NavSatFix, queue_size=1)
		rospy.sleep(8)
		rospy.loginfo("objects initialised for tf repair....")
		rospy.loginfo("repair tf started..")



	def tf_cb(self, data):
		self.last_tf = data

	def do_work(self):
		self.last_tf.header.frame_id = "gps"
		self.tf_pub.publish(self.last_tf)

	def run(self):
		r = rospy.Rate(1)
		while not rospy.is_shutdown():
			self.do_work()
			r.sleep()


if __name__ == '__main__':
	rospy.init_node('frame_repairer')
	obj = FrameRepair()
	obj.run()


