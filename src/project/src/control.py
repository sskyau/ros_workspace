import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def callback(msg):

#if dist to obstacle in front of robot is bigger than 1m, move forward
if msg.ranges[0] > 1:
    move.linear.x = 0.5
    move.angular.z = 0.0

#if dist to obstacle in front of robot is smaller than 1m, stop

print "Number of ranges: " , len(msg.ranges)
print "Reading at position 0: ", msg.ranges[0]

if msg.ranges[0] < 1:
    move.linear.x = 0.0
    move.angular.z = 0.0

pub.publish(move)

rospy.init_node('bot_control')
sub = rospy.Subscriber('/scan', LaserScan, callback) 
pub = rospy.Publisher('/cmd_vel', Twist)
move = Twist()

rospy.spin()

