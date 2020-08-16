#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from math import radians

class DrawASquare():
    def __init__(self):
        rospy.init_node('drawasquare', anonymous=False)
        rospy.on_shutdown(self.shutdown)
        self.cmd_vel = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
     
        r = rospy.Rate(5)
        # create two different Twist() variables.  One for moving forward.  One for turning 45 degrees.
        move_cmd = Twist()# let's go forward at 0.2 m/s
        move_cmd.linear.x = 0.2
        turn_cmd = Twist() #let's turn at 45 deg/s
        turn_cmd.linear.x = 0
        turn_cmd.angular.z = radians(45); #45 deg/s in radians/s

        #two keep drawing squares.  Go forward for 2 seconds (10 x 5 HZ) then turn for 2 second
        count = 0
        while not rospy.is_shutdown():
            rospy.loginfo("Going Straight")# go forward 0.4 m (2 seconds * 0.2 m / seconds)
            for x in range(0,10):
                self.cmd_vel.publish(move_cmd)
                r.sleep()
        
            rospy.loginfo("Turning") # turn 90 degrees
            for x in range(0,10):
                self.cmd_vel.publish(turn_cmd)
                r.sleep()            
            count = count + 1
            if(count == 4): 
                count = 0
            if(count == 0): 
                rospy.loginfo("TurtleBot should be close to the original starting position (but it's probably way off)")
    
    def shutdown(self):
        rospy.loginfo("Stop Drawing Squares")
        self.cmd_vel.publish(Twist())# stop turtlebot
        rospy.sleep(1)
 
if __name__ == '__main__':
    try:
        DrawASquare()
    except:
        rospy.loginfo("node terminated.")


