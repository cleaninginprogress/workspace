#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

class GTTSNode():
  def __init__(self):
    self.sub = rospy.Subscriber("/hand_detection", String, callback=self.gttsCallback)
    rospy.loginfo("Subscribed to /hand_detection")

  def gttsCallback(self, data):
    rospy.loginfo(data)

def main():
  rospy.init_node("gtts_node")

  # create node
  gttsNode = GTTSNode()

  # use node
  rospy.spin()

  # destroy node
  rospy.signal_shutdown()

if __name__ == "__main__":
  try:
    main()
  except rospy.ROSInterruptException:
  	pass