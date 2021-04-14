
#include <Servo.h> 
#include <ros.h>
#include <geometry_msgs/Twist.h>  // For geometry_msgs::Twist



ros::NodeHandle  nh;

Servo servo1;



void messageCb(const geometry_msgs::Twist& msg)
{
  const float x = msg.linear.x;
  const float z_rot = msg.angular.z;

  if (x == 0.1){
    servo1.write(120);
  }
  else if (x==0){
    servo1.write(0);
  }

}


ros::Subscriber<geometry_msgs::Twist> sub("cmd_vel", &messageCb);


void setup()
{ 
  nh.initNode();
  servo1.attach(8,540,2500);
  servo1.write(90);
  nh.subscribe(sub);
  
}

void loop()
{

  nh.spinOnce();
  delay(1);
}
