#!/usr/bin/env python
import rospy
import math
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist

class Odometrymod:
  def __init__(self):
    self.sub = rospy.Subscriber('rtabmap/odom',Odometry,self.Odomdata)
    self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    self.total_distance = 0.
    self.previous_x = 0
    self.previous_y = 0
    self.first_run = True

  def Odomdata(self,msg):
      if (self.first_run):
        self.previous_x = msg.pose.pose.position.x
        self.previous_y = msg.pose.pose.position.y
      x = msg.pose.pose.position.x
      y = msg.pose.pose.position.y
      d_increment = x - self.previous_x
      self.total_distance = self.total_distance + d_increment
      rospy.loginfo(self.total_distance)
      self.previous_x = msg.pose.pose.position.x
      self.previous_y = msg.pose.pose.position.y
      self.first_run = False


      # return self.total_distance
      # print("second")
      self.move_cmd = Twist()

      if (self.total_distance < 1):
        self.move_cmd.linear.x = 0.1
        self.move_cmd.angular.z = 0.0
        self.pub.publish(self.move_cmd)
      else:
        self.move_cmd.linear.x = 0.0
        self.move_cmd.linear.z = 0.0
        self.pub.publish(self.move_cmd)


if __name__ == "__main__":
    rospy.init_node('oodometry', anonymous=True) #make node
    odom = Odometrymod()
    rospy.spin()
