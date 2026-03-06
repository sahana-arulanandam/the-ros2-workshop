#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import sys
import termios
import tty

class RobotController(Node):
    def __init__(self):
        super().__init__('robot_controller')
        
        # Create publisher for cmd_vel topic
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        
        # Velocity parameters
        self.linear_speed = 0.5  # m/s
        self.angular_speed = 1.0  # rad/s
        
        self.get_logger().info('Robot Controller Started')
        self.get_logger().info('Use arrow keys to control the robot:')
        self.get_logger().info('  UP: Move forward')
        self.get_logger().info('  DOWN: Move backward')
        self.get_logger().info('  LEFT: Turn left')
        self.get_logger().info('  RIGHT: Turn right')
        self.get_logger().info('  SPACE: Stop')
        self.get_logger().info('  Q: Quit')
        
    def publish_velocity(self, linear_x, angular_z):
        """Publish velocity command"""
        msg = Twist()
        msg.linear.x = linear_x
        msg.angular.z = angular_z
        self.publisher_.publish(msg)
        
    def stop_robot(self):
        """Stop the robot"""
        self.publish_velocity(0.0, 0.0)

def get_key():
    """Get keyboard input"""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        key = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return key

def main(args=None):
    rclpy.init(args=args)
    
    controller = RobotController()
    
    # Store terminal settings
    settings = termios.tcgetattr(sys.stdin)
    
    try:
        while rclpy.ok():
            key = get_key()
            
            # Arrow keys produce escape sequences
            if key == '\x1b':  # ESC
                next1, next2 = sys.stdin.read(2)
                if next1 == '[':
                    if next2 == 'A':  # UP arrow
                        controller.publish_velocity(controller.linear_speed, 0.0)
                        controller.get_logger().info('Moving forward')
                    elif next2 == 'B':  # DOWN arrow
                        controller.publish_velocity(-controller.linear_speed, 0.0)
                        controller.get_logger().info('Moving backward')
                    elif next2 == 'C':  # RIGHT arrow
                        controller.publish_velocity(0.0, -controller.angular_speed)
                        controller.get_logger().info('Turning right')
                    elif next2 == 'D':  # LEFT arrow
                        controller.publish_velocity(0.0, controller.angular_speed)
                        controller.get_logger().info('Turning left')
            
            elif key == ' ':  # SPACE
                controller.stop_robot()
                controller.get_logger().info('Stopped')
            
            elif key == 'q' or key == 'Q':  # Quit
                controller.get_logger().info('Quitting...')
                break
            
            elif key == '\x03':  # Ctrl+C
                break
    
    except Exception as e:
        controller.get_logger().error(f'Error: {e}')
    
    finally:
        # Restore terminal settings
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
        controller.stop_robot()
        controller.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
