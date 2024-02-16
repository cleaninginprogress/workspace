#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
import os
from gtts import gTTS

topicName = "hand_detection_result"

class GTTSNode():
  def __init__(self):
    self.sub = rospy.Subscriber(topicName, String, callback=self.gttsCallback)

  def gttsCallback(self, data):
    rospy.loginfo("Hand detection result: %s", data.data)
    mytext = 'Welcome to AI for robotics!'
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("welcome.mp3")
    os.system("sudo mpg321 welcome.mp3")

def main():
  rospy.init_node("gtts_node")

  # create node
  GTTSNode()

  # use node
  rospy.spin()

  # destroy node
  rospy.signal_shutdown()

if __name__ == "__main__":
  try:
    main()
  except rospy.ROSInterruptException:
  	pass