#!/usr/bin/env python

import roslib;roslib.load_manifest('dynamic_reconfigure')
import rospy

import dynamic_reconfigure
# from dynamic_reconfigure import client
# from dynamic_reconfigure import *
# import dynamic_reconfigure.client
# from dynamic_reconfigure.client import Client
# from dynamic_reconfigure.dynamic_reconfigure.server import Server

if __name__ == "__main__":
    rospy.init_node("dynamic_reconfigure")
    print(dir(dynamic_reconfigure))
    client = dynamic_reconfigure.client.Client("move_base/DWAPlannerROS", timeout=4, config_callback=None)

    r = rospy.Rate(0.33)
    while not rospy.is_shutdown():
        client.update_configuration({"/move_base/DWAPlannerROS/yaw_goal_tolerance":0.17})
        r.sleep()