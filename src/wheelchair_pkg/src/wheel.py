#!/usr/bin/env python
import rospy
import math
from nav_msgs.msg import Odometry
from wheelchairCtrl.msg import joyStick
import serial

class Odometrymod:
  def __init__(self):
    self.sub = rospy.Subscriber('odom',Odometry,self.Odomdata)
    self.pub = rospy.Publisher('wheelchair_drive', joyStick, queue_size=10)
    self.ser = serial.Serial('/dev/ttyUSB0',115200)   # USB connceted property
    self.get_arduino_msg()
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
      d_increment = math.sqrt((x - self.previous_x) * (x - self.previous_x) + (y - self.previous_y)*(y - self.previous_y))
      self.total_distance = self.total_distance + d_increment
      print(self.total_distance)
      self.previous_x = msg.pose.pose.position.x
      self.previous_y = msg.pose.pose.position.y
      self.first_run = False
      #print("second")
      self.move_cmd = joyStick()

      if (self.total_distance < 1):
        self.move_cmd.linear = 0.1
        self.move_cmd.angular = 0.0
        self.pub.publish(self.move_cmd)
      else:
        self.move_cmd.linear = 0.0
        self.move_cmd.angular = 0.0
        self.pub.publish(self.move_cmd)

  def send_cmd_arduino (self,move_cmd):
      speed = move_cmd.linear.x
      turn = move_cmd.angular.z
      message = "{},{}*".format(straight,turn)
      print(message)
      self.ser.write(message)

  def get_arduino_msg(self):
      pub = rospy.Publisher('arduino', String,queue_size = 10)
      r = rospy.Rate(10)
      while not rospy.is_shutdown():
          message = self.ser.readline()
          pub.publish(message)
          r.sleep()




if __name__ == "__main__":
    rospy.init_node('oodometry', anonymous=True) #make node
    odom = Odometrymod()
    rospy.spin()
