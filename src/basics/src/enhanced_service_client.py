#!/usr/bin/env python

import rospy

from basics.srv import WordCount
from std_msgs.msg import String

import sys


rospy.init_node('service_client')

rospy.wait_for_service('word_count')

words = ' '.join(sys.argv[1:])


word_counter = rospy.ServiceProxy('word_count', WordCount)

try:
    word_count = word_counter(words)
except:
    print("word count service error")

print words, '->', word_count.count

try:
    pub = rospy.Publisher('count_word_pub', String, queue_size=2)
    pub.publish(words)
    print("publishing " + words)
except:
    print("error in publishing")


#print words, '->', word_count.count, word_count.len_count

