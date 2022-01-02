#!/usr/bin/env python2

import rospy
from sensor_msgs.msg import Range
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from rosgraph_msgs.msg import Clock
import math
import message_filters
from sensor_msgs.msg import LaserScan


isFirstRun = True

old_x = 0.0
old_y = 0.0
dist = 0.0

def laser_callback(msg, odom_msg, fl_msg, fr_msg):

    
    calc_dist_travelled(odom_msg)

    #print(len(msg.ranges))
    regions = {
        #'right': min(min(msg.ranges[0:143]),10),
        #'fr': min(min(msg.ranges[144:287]), 10), 
        #'front': min(min(msg.ranges[288:431]),10),
        #'fl': min(min(msg.ranges[432:575]), 10),
        #'left': min(min(msg.ranges[576:713]), 10),
        'a': msg.ranges[0],
        'b': min(msg.ranges[89:179]),
        'c': msg.ranges[360],
        'd': min(msg.ranges[539:629])
    }

    if math.isinf(regions['b']):
        regions['b'] = 8

    if math.isinf(regions['d']):
        regions['d'] = 8

    z = odom_msg.pose.pose.orientation.z
    w = odom_msg.pose.pose.orientation.w

    print("fl range: " + str(fl_msg.range))
    print("fr range: " + str(fr_msg.range))

    take_action(regions, z, w, fl_msg.range, fr_msg.range)

def take_action(regions, z, w, fl, fr):
    print()
    print("a 0: " + str(regions['a']))
    print("b 180: " + str(regions['b']))
    print("c back: " + str(regions['c']))
    print("d 540: " + str(regions['d']))
    print("z: " + str(z))
    print("w: " + str(w))

    #print("left: " + str(regions['left']))
    #print("fl: " + str(regions['fl']))
    #print("front: " + str(regions['front']))
   # print("fr: " + str(regions['fr']))
    #print("right: " + str(regions['right']))

    orient_thres = 0.95
    lidar_thres = 1.5
    ir_thres = 0.7

    # if there is obtacle in front and detectable by laser scanner
    if regions['a'] < lidar_thres:
        move.linear.x = 0
        move.angular.z = 0
        pub.publish(move)
    
        #if left obtacle closer than right obstacle, turn right
        if regions['b'] < regions['d']: 
            print("left obstacle is closer than right obstacle, turn right")
            move.linear.x = 0
            move.angular.z = -2

        #if right obstacle closer than or equal to right obstacle, turn right
        else:
            print("right obstacle closer than/equal to left obstacle, turn left")
            move.linear.x = 0
            move.angular.z = 2
    
    # if there is obstacle in front detected by infrared sensor
    elif fl < ir_thres:
        if fl < fr:
            print("front left obstacle detected by infrared, turn right")
            move.linear.x = 0
            move.angular.z = -2

    elif fr < ir_thres:
        if fr < fl:
            print("front right obstacle detected by infrared, turn left")
            move.linear.x = 0
            move.angular.z = 2

    else:
        # TODO: adjust direction
        if abs(z) < orient_thres and z*w > 0 and regions['b'] > lidar_thres:
        #if abs(w) > 0.15 and z * w > 0 and regions['b'] > 2:
            print("turning left to face towards goal")
            move.linear.x = 0.0
            move.angular.z = 0.0
            pub.publish(move)

            move.linear.x = 0.0
            move.angular.z = 2.0

        elif abs(z) > orient_thres and z*w < 0 and regions['d'] > lidar_thres:
         #elif abs(w) > 0.15 and z * w < 0 and regions['d'] > 2:
            print("turning right to face towards goal")
            move.linear.x = 0.0
            move.angular.z = 0.0
            pub.publish(move)

            move.linear.x = 0.0
            move.angular.z = -2.0

        else:
            print("no obstacle")
            move.linear.x = 0.5
            move.angular.z = 0

    pub.publish(move)

    
def calc_dist_travelled(msg):
    global isFirstRun
    global dist 
    global old_x
    global old_y   
     
    if isFirstRun ==  True:
        old_x = round(msg.pose.pose.position.x*100.0)/100.0
        old_y = round(msg.pose.pose.position.y*100.0)/100.0

    new_x = round(msg.pose.pose.position.x*100.0)/100.0
    new_y = round(msg.pose.pose.position.y*100.0)/100.0

    dist = dist + math.sqrt((new_x - old_x)**2 + (new_y - old_y)**2)
    old_x = new_x
    old_y = new_y
    isFirstRun = False 

    print("Distance travelled: " + str(dist))

def clock_callback(msg):
    print("Simulation Time: " + str(msg.clock.secs) + " secs")

rospy.init_node('bot_control')
move = Twist()

print("node activated")

sub_fl = message_filters.Subscriber('/range/fl', Range)
sub_fr = message_filters.Subscriber('/range/fr', Range)
#sub_rl = message_filters.Subscriber('/range/rl', Range)
#sub_rr = message_filters.Subscriber('/range/rr', Range)
sub_odom = message_filters.Subscriber('/odom',  Odometry)

#ts = message_filters.ApproximateTimeSynchronizer([sub_fl, sub_fr, sub_rl, sub_rr, sub_odom], 1,1)
#ts.registerCallback(ts_callback)

sub_clock = rospy.Subscriber('/clock', Clock, clock_callback)

pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

laser_sub = message_filters.Subscriber('/scan', LaserScan)
ts = message_filters.ApproximateTimeSynchronizer([laser_sub, sub_odom, sub_fl, sub_fr], 1,1)
ts.registerCallback(laser_callback)

#print("Simulation time: " + str(simTime))
#print("Cumulative distance travelled: " + str(dist))

rospy.spin()

