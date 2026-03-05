from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld=LaunchDescription()

    joystick_node=Node(package='joystick_node',
                       executable='joystick_node',
                       name='joystick_node',
                       output='screen')

    ld.add_action(joystick_node)

    return ld