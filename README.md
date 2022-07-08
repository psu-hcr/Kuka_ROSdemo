# Kuka_ROSdemo
A demo package using ROS to control the Kuka iiwa LBR

Requirements
-----------

Use of the ROS_Template requires several packages to be installed and a file structure in place:

* [ROS] - The Robot Operating System
* A catkin workspace - Setup a new workspace with these commands
`mkdir chosenname_ws && cd chosenname_ws && mkdir src`
`catkin_init_workspace`
* [iiwa_ros] - A metapackage developed to control the Kuka with ROS. The metapackage should reside in the same workspace as this package.

Dependencies
-------------


	
[ROS]: http://www.ros.org
[iiwa_stack]: https://github.com/epfl-lasa/iiwa_ros
[ROS_Template]: https://github.com/psu-hcr/ROS_Template