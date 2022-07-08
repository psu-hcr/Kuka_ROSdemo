"""
Kathleen Fitzsimons
This node sends a command to the Kuka to move along the path of an ellipse.
Impedance control options are selected. However, the trajectory terminates when 
person's interact too forcefully with the end effector.
SUBSCRIBERS:
    - cursor_state (/robot/limb/right/endpoint_state)
    - traj_result (/motion/motion_command/result)
PUBLISHERS:N/A
 
SERVICES:
    - iiwa_ros's Forward Kinematic Server is used by setting up
      a client called (ac) publishing commands to the topic
      /iiwa/iiwa_fk_server
"""
from iiwa_tools.srv import GetFK
import rospy
from std_msgs.msg import Float64MultiArray, MultiArrayLayout, MultiArrayDimension

fk_service = '/iiwa/iiwa_fk_server'
rospy.wait_for_service(fk_service)
get_fk = rospy.ServiceProxy(fk_service, GetFK)
seed = Float64MultiArray()
seed.layout = MultiArrayLayout()
seed.layout.dim = [MultiArrayDimension(), MultiArrayDimension()]
seed.layout.dim[0].size = 1
seed.layout.dim[1].size = 7
seed.data = [0., 0., 0., 0., 0., 0., 0.]
resp = get_fk(joints=seed)
sol_pose = resp.poses[0]
print('sol:', sol_pose)

