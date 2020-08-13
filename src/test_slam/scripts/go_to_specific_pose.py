#!/usr/bin/env python

import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib
from actionlib_msgs.msg import *
from geometry_msgs.msg import Pose, Point, Quaternion

class GoToPose():
    def __init__(self):
        self.goal_sent = False
        rospy.on_shutdown(self.shutdown)# What to do if shut down (e.g. Ctrl-C or failure)
        self.move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)# Tell the action client that we want to spin a thread by default
        rospy.loginfo("Wait for the action server to come up")
        self.move_base.wait_for_server(rospy.Duration(5))# Allow up to 5 seconds for the action server to come up

    def goto(self, pos, quat):
        self.goal_sent = True # Send a goal
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = 'map'
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose = Pose(Point(pos['x'], pos['y'], 0.000), Quaternion(quat['r1'], quat['r2'], quat['r3'], quat['r4']))

        self.move_base.send_goal(goal) # Start moving
        success = self.move_base.wait_for_result(rospy.Duration(60)) # Allow TurtleBot up to 60 seconds to complete task
        state = self.move_base.get_state()
        result = False

        if success and state == GoalStatus.SUCCEEDED:
            result = True # We made it!
        else:
            self.move_base.cancel_goal()

        self.goal_sent = False
        return result

    def shutdown(self):
        if self.goal_sent:
            self.move_base.cancel_goal()
        rospy.loginfo("Stop")
        rospy.sleep(1)

if __name__ == '__main__':
    try:
        rospy.init_node('nav_test', anonymous=False)
       
        position = {'x': 0.00, 'y' : 2.00}  # Customize the following values so they are appropriate for your location
        quaternion = {'r1' : 0.000, 'r2' : 0.000, 'r3' : 0.000, 'r4' : 1.000}
        rospy.loginfo("Go to (%s, %s) pose", position['x'], position['y'])
        
        # navigator = GoToPose()
        success = GoToPose().goto(position, quaternion)

        if success:
            rospy.loginfo("Hooray, reached the desired pose")
        else:
            rospy.loginfo("The base failed to reach the desired pose")
        
        rospy.sleep(1) # Sleep to give the last log messages time to be sent

    except rospy.ROSInterruptException:
        rospy.loginfo("Ctrl-C caught. Quitting")