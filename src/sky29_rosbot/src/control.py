#! /usr/bin/env python

import rospy
from sensor_msgs.msg import Range
from geometry_msgs.msg import Twist

fl_range = 0.899
fr_range = 0.899

def consol_sensor_ranges(fl_range, fr_range):
    if fl_range < 0.6 and fr_range > 0.6:
        move.linear.x = 0
        move.angular.z = 0
        pub.publish(move)

        move.linear.x = 0.0
        move.angular.z = -1.0
   
    elif fl_range > 0.6 and fr_range < 0.6:
        move.linear.x = 0
        move.angular.z = 0
        pub.publish(move)


        move.linear.x = 0.0
        move.angular.z = 1.0
    
    elif fl_range < 0.6 and fr_range < 0.6:
        move.linear.x = 0
        move.angular.z = 0
        pub.publish(move)

        move.linear.x = -0.5
        move.angular.z = 0.0

    else:
        move.linear.x = 0.5
        move.angular.z = 0.0

    print("consolidated fl_range: " + str(fl_range))
    print("consolidated fr_range: " + str(fr_range))
    print("move linear x: " + str(move.linear.x))
    print("move angular.z: " + str(move.angular.z))

    return move

def fl_callback(msg):

    fl_range = msg.range
    print("fl: " + str(msg.range))

def fr_callback(msg):
    fr_range = msg.range
    print("fr: " + str(msg.range))
    move = consol_sensor_ranges(fl_range, msg.range)
    pub.publish(move)

#fl_range = 0.899
#fr_range = 0.899
rospy.init_node('bot_control')
move = Twist()
sub_fl = rospy.Subscriber('/range/fl', Range , fl_callback)
sub_fr = rospy.Subscriber('/range/fr', Range , fr_callback)
pub = rospy.Publisher('/cmd_vel', Twist)

rospy.spin()

