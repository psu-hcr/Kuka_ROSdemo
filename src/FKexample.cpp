/*
Kathleen Fitzsimons
This node sends a command to the Kuka to move along the path of an ellipse.
Impedance control options are selected. However, the trajectory terminates when 
person's interact too forcefully with the end effector.
SUBSCRIBERS:
    - cursor_state (/robot/limb/right/endpoint_state)
    - traj_result (/motion/motion_command/result)
PUBLISHERS:N/A
 
SERVICES:
    -  iiwa_ros's Forward Kinematic Server is used by setting up
      a client called (ac) publishing commands to the topic
      /iiwa/iiwa_fk_server
*/
#include <ros/ros.h>
#include <iostream>
#include <ros/console.h>
#include <geometry_msgs/Pose.h>
#include <tf2_geometry_msgs/tf2_geometry_msgs.h>

//For getting the end point position and orientation
#include <intera_motion_msgs/MotionCommandAction.h>
#include <actionlib/client/simple_action_client.h>

//Custom includes
#include "KukaROS_Demos/Eeffector.h"

