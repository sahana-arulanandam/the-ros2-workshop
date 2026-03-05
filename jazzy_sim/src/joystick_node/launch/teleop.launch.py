from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([

        # Joystick driver
        Node(
            package='joy',
            executable='joy_node',
            name='joy_node',
            output='screen',
            parameters=[{
                'axis_linear.x': 1,           # left stick forward/back
                'axis_angular.yaw': 2,        # right stick left/right
                'require_enable_button': False
            }]
        ),

        # Teleop translator
        Node(
            package='teleop_twist_joy',
            executable='teleop_node',
            name='teleop_twist_joy_node',
            output='screen',
            parameters=[{
                'axis_linear.x': 1,           # left stick forward/back
                'axis_angular.yaw': 2,        # right stick left/right
                'require_enable_button': False
                'max_x_vel': 30.0,
                'max_yaw_vel': 1.0
            }]
        ),
    ])

