#!/usr/bin/env python
# BEGIN ALL
#!/usr/bin/env python


import rospy
from std_msgs.msg import Int32
from std_msgs.msg import String

# BEGIN CALLBACK
def callback(msg):
    print msg.data
# END CALLBACK


rospy.init_node('enhanced_topic_subscriber')

# BEGIN SUBSCRIBER
sub = rospy.Subscriber('word_counter', String, callback)
# END SUBSCRIBER

rospy.spin()
# END ALL
