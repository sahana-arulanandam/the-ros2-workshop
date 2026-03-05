from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node
import os

def generate_launch_description():

    urdf_path = PathJoinSubstitution([
        FindPackageShare('my_robot_description'),
        'urdf',
        'my_robot.urdf.xacro'
    ])

    gazebo_config_path = PathJoinSubstitution([
        FindPackageShare('my_robot_bringup'),
        'config',
        'gazebo_bridge.yaml'
    ])

    rviz_config_path = PathJoinSubstitution([
        FindPackageShare('my_robot_description'),
        'rviz',
        'urdf_config.rviz'
    ])

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{
                'robot_description': Command(['xacro ', urdf_path])
            }]
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                PathJoinSubstitution([
                    FindPackageShare('ros_gz_sim'),
                    'launch',
                    'gz_sim.launch.py'
                ])
            ),
            launch_arguments={'gz_args': 'empty.sdf -r'}.items()
        ),

        Node(
            package='ros_gz_sim',
            executable='create',
            arguments=['-topic', 'robot_description']
        ),

        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            parameters=[{'config_file': gazebo_config_path}]
        ),

        Node(
            package='rviz2',
            executable='rviz2',
            arguments=['-d', rviz_config_path]
        ),

        Node(
            package="joint_state_publisher_gui",
            executable="joint_state_publisher_gui"
        )

    ])
