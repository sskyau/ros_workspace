#! /usr/bin/env python

import rospy
from sensor_msgs.msg import Range
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from rosgraph_msgs.msg import Clock
import math

fl_range = 0.899
fr_range = 0.899

isFirstRun = True

new_x = 0.0
new_y = 0.0
dist = 0.0
simTime = 0.0

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

def odom_callback(odom_data):

    if isFirstRun ==  True:
        old_x = round(msg.pose.pose.position.x*100.0)/100.0
        old_y = round(msg.pose.pose.position.y*100.0)/100.0

    new_x = round(msg.pose.pose.pose.position.x*100.0)/100.0
    new_y = round(msg.pose.pose.pose.position.y*100.0)/100.0

    dist = dist + math.sqrt((new_x - old_x)**2 + (new_y - old_y)**2)
    old_x = new_x
    old_y = new_y
    isFirstRun = False 

    print("z: ", odom_data.pose.pose.orientation.z)
    print("w: ", odom_data.pose.pose.orientation.w)

def clock_callback(msg):
    simTime = msg.clock

#fl_range = 0.899
#fr_range = 0.899
rospy.init_node('bot_control')
move = Twist()
sub_fl = rospy.Subscriber('/range/fl', Range , fl_callback)
sub_fr = rospy.Subscriber('/range/fr', Range , fr_callback)
sub_odom = rospy.Subscriber('/odom',  Odometry, odom_callback)

sub_clock = rospy.Subscriber('/clock', Clock, clock_callback)

pub = rospy.Publisher('/cmd_vel', Twist)

print("Simulation time: " + str(simTime))
print("Cumulative distance travelled: " + str(dist))

rospy.spin()

