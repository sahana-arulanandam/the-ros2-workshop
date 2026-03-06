#!/usr/bin/env python3
import os
import xacro
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
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
    
    # RViz config file
    rviz_config_file = os.path.join(pkg_two_wheel, 'rviz', 'display.rviz')
    
    # 1. Launch Gazebo
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gazebo.launch.py')
        ),
        launch_arguments={
            'verbose': 'true',
            'pause': 'false'
        }.items()
    )
    
    # 2. Robot State Publisher (shared by both RViz and Gazebo)
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{
            'robot_description': robot_description,
            'use_sim_time': True  # IMPORTANT: True for Gazebo sync
        }]
    )
        

    
    # 4 Spawn Robot in Gazebo
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
    
    # 5. RViz Node
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', rviz_config_file],
        parameters=[{'use_sim_time': True}]  # Sync with Gazebo time
    )
    
    return LaunchDescription([
        gazebo,
        robot_state_publisher,
        TimerAction(
            period=3.0,  # Wait 3 seconds for Gazebo to start
            actions=[spawn_entity]
        ),
        TimerAction(
            period=5.0,  # Wait 5 seconds before launching RViz
            actions=[rviz_node]
        )
    ])
