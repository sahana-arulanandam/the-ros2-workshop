#!/usr/bin/python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

class JoystickController(Node):

    def __init__(self):
        super().__init__('joystick_controller')
        
        self.cmd_vel_pub=self.create_publisher(Twist,
                                               'cmd_vel',
                                               1)
        
        self.create_subscription(Joy,
                                 'joy',
                                 self.joystick_cb,
                                 1)
        
        self.declare_parameter('max_x_vel',value=0.5)
        self.declare_parameter('max_yaw_vel',value=1.0)

        self.max_xvel=self.get_parameter('max_x_vel').value
        self.max_yawvel=self.get_parameter('max_yaw_vel').value
    
        self.enable_control=False
        self.prev_state_enable_btn=False
        self.get_logger().info(f"Max-Xvel:{self.max_xvel} Max-Yawvel:{self.max_yawvel}")
        self.get_logger().info(f'Control:{self.enable_control}')

    def joystick_cb(self,data:Joy):
        x_vel=data.axes[1]*self.max_xvel
        yaw_vel=data.axes[3]*self.max_yawvel

        if self.enable_control:
             self.create_and_publish_twist_msg(x_vel,yaw_vel)

        if data.buttons[9]==1 and data.buttons[9]!=self.prev_state_enable_btn:
                self.enable_control= not self.enable_control
                self.get_logger().info(f'Control:{self.enable_control}')
        self.prev_state_enable_btn=data.buttons[9]

    def create_and_publish_twist_msg(self,x_vel:float,yaw_vel:float):
        msg=Twist()
        msg.linear.x=x_vel
        msg.angular.z=yaw_vel

        self.cmd_vel_pub.publish(msg)


def main(args=None):

    rclpy.init(args=args)
    joystick_node=JoystickController()
    rclpy.spin(joystick_node)

    joystick_node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
     main()

