#!/usr/bin/env python3
from launch.actions import SetEnvironmentVariable
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, ExecuteProcess
import xacro
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    
    # Package paths
    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
    pkg_two_wheel = get_package_share_directory('two_wheel')
    
    # URDF file path
    urdf_file = os.path.join(pkg_two_wheel, 'urdf', 'two_wheel.urdf')

    # Read URDF content
    with open(urdf_file, 'r') as f:
        robot_description = f.read()
    
    robot_description = xacro.process_file(urdf_file).toxml()


    # Gazebo launch with proper parameters
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gazebo.launch.py')
        ),
        launch_arguments={
            'verbose': 'true',
            'pause': 'false'
        }.items()
    )
    
    # Robot state publisher
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{
            'robot_description': robot_description,
            'use_sim_time': True
        }]
    )
    
    # Spawn entity
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-topic', '/robot_description',
            '-entity', 'two_wheel_robot',
            '-x', '0.0',
            '-y', '0.0',
            '-z', '0.1',
            '-timeout', '120.0'
        ],
        output='screen'
    )
    
    return LaunchDescription([
        gazebo,
        robot_state_publisher,
        spawn_entity
    ])
