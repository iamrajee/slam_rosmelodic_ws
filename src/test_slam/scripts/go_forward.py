#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

class GoForward():
    def __init__(self):
        rospy.init_node('GoForward', anonymous=False)

	rospy.loginfo("To stop TurtleBot CTRL + C")
    rospy.on_shutdown(self.shutdown) #run self.shutdown on shutdown
        
    self.cmd_vel = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    move_cmd = Twist()	
    move_cmd.linear.x = 0.2 #x_velocity 0.2 m/s
	move_cmd.angular.z = 0
    r = rospy.Rate(10)

    while not rospy.is_shutdown():
        self.cmd_vel.publish(move_cmd)
        r.sleep()
        
    def shutdown(self):
        rospy.loginfo("Stop TurtleBot")
        self.cmd_vel.publish(Twist())# by default Twist() has all field 0, so stops!
        rospy.sleep(1)
 
if __name__ == '__main__':
    try:
        GoForward()
    except:
        rospy.loginfo("GoForward node terminated.")
