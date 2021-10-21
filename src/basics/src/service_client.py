#!/usr/bin/env python

import rospy

from basics.srv import WordCount

import sys


rospy.init_node('service_client')

rospy.wait_for_service('word_count')

words = ' '.join(sys.argv[1:])

h = {'words': words}

word_counter = rospy.ServiceProxy('word_count', WordCount, headers=h)

word_count = word_counter(words)

print words, '->', word_count.count

#print words, '->', word_count.count, word_count.len_count

