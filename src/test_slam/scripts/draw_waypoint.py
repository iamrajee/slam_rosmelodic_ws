#!/usr/bin/env python
import rospy
import numpy as np
import tf
import math
import geometry_msgs.msg
from geometry_msgs.msg import Point
from visualization_msgs.msg import Marker

class waypoint(object):
	def __init__(self):
		self.marker_id = 0

		self.path = Marker()
		self.path.header.frame_id = "/map"	# publish path in map frame
		self.path.type = self.path.LINE_STRIP
		self.path.action = self.path.ADD
		self.path.lifetime = rospy.Duration(0)
		self.path.scale.x = 0.05
		self.path.color.a = 1.0
		self.path.color.r = 0.0
		self.path.color.g = 1.0
		self.path.color.b = 0.0
		self.path.pose.orientation.w = 1.0

		self.points = Marker()		
		self.points.header.frame_id = "/map"	# publish path in map frame		
		self.points.type = self.points.POINTS
		self.points.action = self.points.ADD
		self.points.lifetime = rospy.Duration(0)
		self.points.scale.x = 0.1
		self.points.scale.y = 0.1	
		self.points.color.a = 1.0
		self.points.color.r = 0.0
		self.points.color.g = 0.0
		self.points.color.b = 1.0
		self.points.pose.orientation.w = 1.0

		
		rospy.init_node('MarkerPublisher')
		rospy.Subscriber("/move_base_simple/goal2", geometry_msgs.msg.PoseStamped, self.get_way_point) # subscribe to "/move_base_simple/goal" to get picked way points using 2D Nav Goal in rviz
		self.publisher = rospy.Publisher('visualization_marker', Marker, queue_size = 10)# display picked way points and path between way points in rviz

	# fetch clicked way points
	def get_way_point(self, msg):
		self.marker_id += 1
		# display way points and path on the map
		self.display_way_point(msg.pose.position.x,msg.pose.position.y)
		self.display_path(msg.pose.position.x,msg.pose.position.y)

		# get orientationn and convert quternion to euler (roll pitch yaw)
		quaternion = ( msg.pose.orientation.x, msg.pose.orientation.y, msg.pose.orientation.z, msg.pose.orientation.w)
		euler = tf.transformations.euler_from_quaternion(quaternion)
		yaw = math.degrees(euler[2])
		print("X " , msg.pose.position.x, "m Y ", msg.pose.position.y, " m Yaw ", yaw, "degrees")

	# display way points on the map
	def display_way_point(self,x,y):
		self.points.id = self.marker_id
		point = Point()
		point.x,point.y = x,y
		self.points.points.append(point)
		self.publisher.publish(self.points)

	# display path between way points on the map
	def display_path(self,x,y):
		self.points.id = self.marker_id
		point = Point()
		point.x,point.y = x,y
		self.path.points.append(point)
		self.publisher.publish(self.path) # Publish the path

	def run(self):
		rospy.spin()

if __name__ == '__main__':
	print "*********** waypoint.py: read and display way point on the map ***********"
	waypoint().run()