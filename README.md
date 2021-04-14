# ROS_Arduino_interface
This repository contains the ROS-Arduini interface code required to implement the automated joystick control for wheelchair.
## Task 1 - Run wheelchair for 1 meter automatically
1. To know the position of wheelchair, realsense depth camera is used to launch Rtab map SLAM and using ```/rtab/odom``` topic postion is obtained. 
2. Based on position of the wheelchair, distance is calculated from the start point and current position of the wheelchair and ```/cmd_vel``` topic is published accordingly.
3. In arduino script, the subcriber subscribes to this cmd_vel topic and set the angle of the servo motor which is connected to joystick of the wheelchair.
4. To launch the file which runs ros script and arduio serial node,__
```roslaunch wheelchair_pkg wheelchair.launch ```
5. Note that, the arduino script need to be uploaded on Arduino. 

## Implementation
![video](https://github.com/Praj390/ROS_Arduino_interface/blob/main/src/wheelchair_pkg/tutorial.gif) 
