#!/usr/bin/env python3
import rospy
from audio_common_msgs.msg import AudioData

class SpeechToTextNode:
    def __init__(self):
        self.sub = rospy.Subscriber('/audio/audio', AudioData, callback=self.speechToTextCallback)
        rospy.loginfo('Subscribed to /audio/audio')

    def speechToTextCallback(self, msg):
        rospy.loginfo(msg.data)

def main():
    rospy.init_node('speech_to_text_node')

    # create node
    speechToTextNode = SpeechToTextNode()

    # use node
    rospy.spin()

    # destroy node
    rospy.signal_shutdown()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
      	pass

