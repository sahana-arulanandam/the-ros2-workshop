#!/usr/bin/env python3
import os
from launch import LaunchDescription
from launch.actions import ExecuteProcess, TimerAction
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Package directory
    two_wheel_pkg = get_package_share_directory('two_wheel')
    
    # Path to URDF file
    urdf_file = os.path.join(two_wheel_pkg, 'urdf', 'two_wheel.urdf')
    
    # Read URDF file
    with open(urdf_file, 'r') as f:
        robot_desc = f.read()
    
    # Use the custom world file or default empty world
    world_file = os.path.join(two_wheel_pkg, 'worlds', 'empty.world')
    if not os.path.exists(world_file):
        # Fallback to system default
        world_file = '/usr/share/gazebo-11/worlds/empty.world'
    
    # Start Gazebo server with proper world path
    gzserver = ExecuteProcess(
        cmd=['gzserver', 
             world_file,
             '--verbose',
             '-s', 'libgazebo_ros_init.so', 
             '-s', 'libgazebo_ros_factory.so'],
        output='screen',
        additional_env={'LIBGL_ALWAYS_SOFTWARE': '1'}
    )
    
    # Start Gazebo client (GUI)
    gzclient = ExecuteProcess(
        cmd=['gzclient', '--verbose'],
        output='screen',
        additional_env={'LIBGL_ALWAYS_SOFTWARE': '1'}
    )
    
    # Robot state publisher
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{
            'robot_description': robot_desc, 
            'use_sim_time': True
        }]
    )
    
    # Static transform
    static_tf = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='tf_footprint_base',
        arguments=['0', '0', '0', '0', '0', '0', 'base_link', 'base_footprint']
    )
    
    # Spawn entity with delay
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-entity', 'two_wheel',
            '-topic', 'robot_description',
            '-x', '0',
            '-y', '0',
            '-z', '0.2'
        ],
        output='screen'
    )
    
    return LaunchDescription([
        gzserver,
        gzclient,
        robot_state_publisher,
        static_tf,
        TimerAction(
            period=3.0,
            actions=[spawn_entity]
        )
    ])
