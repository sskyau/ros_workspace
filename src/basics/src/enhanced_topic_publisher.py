#!/usr/bin/env python
# BEGIN ALL
# BEGIN SHEBANG
#!/usr/bin/env python
# END SHEBANG

# BEGIN IMPORT
import rospy
import sys
# END IMPORT

# BEGIN STD_MSGS
from std_msgs.msg import Int32
from std_msgs.msg import String
# END STD_MSGS

#BEGIN BASICS
from basics.srv import WordCount, WordCountResponse, WordCountRequest
#END BASICS

rospy.init_node('enhanced_topic_publisher')

#BEGIN PUB
pub = rospy.Publisher('word_counter', String, queue_size=2)
# END PUB


def count_words(request):
    pub.publish("I am counting words: " + request.words + " count: " + str(len(request.words.split())))
    return len(request.words.split())

service = rospy.Service('word_count', WordCount, count_words)

#rospy.wait_for_service("word_count")
'''
words = ''.join(sys.argv[1:])

word_counter = rospy.ServiceProxy('word_count', WordCount)
word_count = word_counter(words)
'''
# BEGIN LOOP
#rate = rospy.Rate(2)

'''
def callback(msg):
    print("in callback function")
    pub.publish("count: " + str(msg.data))
    print(msg.data)
'''
'''
while not rospy.is_shutdown():
    #sub = rospy.Subscriber('count_word_pub', String, callback)
    pub.publish("counting words: " request.words)    

    rate.sleep()
'''
# END LOOP

rospy.spin()

# END ALL
