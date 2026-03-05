from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([

        Node(
            package='joy',
            executable='joy_node',
            name='joy_node',
            output='screen',
            parameters=[{
                'axis_linear.x': 1,
                'axis_angular.yaw': 2,
                #'require_enable_button': False
                #ros2 param set /teleop_twist_joy_node enable_button 10
            }]
        ),

    ])
