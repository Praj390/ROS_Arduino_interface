#!/usr/bin/env python
import rospy
import math
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from tf.transformations import euler_from_quaternion, quaternion_from_euler


global roll, pitch, yaw


class Odometrymod:
  def __init__(self):
    self.sub = rospy.Subscriber('/odom',Odometry,self.Odomdata)
    self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    self.total_distance = 0.
    self.previous_x = 0
    self.previous_y = 0
    self.first_run = True

  def Odomdata(self,msg):
      self.move_cmd = Twist()
      if (self.first_run):
        self.previous_x = msg.pose.pose.position.x
        self.previous_y = msg.pose.pose.position.y

      self.first_run = False
      count = 0
      x = msg.pose.pose.position.x
      y = msg.pose.pose.position.y

      orientation_q = msg.pose.pose.orientation
      orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
      (roll, pitch, yaw) = euler_from_quaternion (orientation_list)
      end = 0
      if count == 0 and end == 0:
          self.move_cmd.linear.x = 0.7
          self.move_cmd.angular.z = 0.7
          self.pub.publish(self.move_cmd)
          print(yaw)




if __name__ == "__main__":
    rospy.init_node('oodometry', anonymous=True) #make node
    odom = Odometrymod()
    rospy.spin()
