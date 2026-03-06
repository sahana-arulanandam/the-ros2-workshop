# Two-Wheel Differential Drive Robot - ROS2 Project Context

## Project Overview
- **Package Name:** two_wheel
- **ROS2 Distribution:** Humble
- **Purpose:** URDF practice and Gazebo simulation
- **Robot Type:** 2-wheel differential drive with lidar sensor
- **Repository Name:** urdf_gazebo

## Project Structure
```
two_wheel/
├── launch/
│   ├── two_wheel_display.launch.py      # RViz only
│   ├── two_wheel_gazebo.launch.py       # Gazebo only
│   ├── two_wheel_sim.launch.py          # Gazebo with custom setup
│   └── rviz_gazebo_combined.launch.py   # Both RViz + Gazebo
├── meshes/                              # STL files for robot
├── rviz/display.rviz                    # RViz configuration
├── two_wheel/robot_controller.py        # Keyboard control node
├── urdf/two_wheel.urdf                  # Robot description
├── worlds/empty.world                   # Gazebo world
├── package.xml                          # Package metadata
└── setup.py                             # Python package setup
```

## Key Features
1. Robot visualization in RViz
2. Gazebo simulation with physics
3. Keyboard teleop control
4. Differential drive controller
5. Lidar sensor (360° scan, 10m range)

## Dependencies
- rclpy, geometry_msgs, sensor_msgs, tf2_ros
- robot_state_publisher, joint_state_publisher_gui
- rviz2, gazebo_ros

## Robot Specifications
- **Wheel Separation:** 0.22184 m
- **Wheel Diameter:** 0.07 m
- **Lidar:** 360 samples, 0.12-10m range, 10Hz update
- **Mass:** Chassis 6.8782 kg, Wheels 0.11545 kg each

## Bashrc Configuration
```bash
source /opt/ros/humble/setup.bash
source /usr/share/gazebo/setup.bash
source $HOME/ros2_ws/install/setup.bash
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:$HOME/ros2_ws/install/two_wheel/share/two_wheel
export GAZEBO_RESOURCE_PATH=$GAZEBO_RESOURCE_PATH:$HOME/ros2_ws/install/two_wheel/share/two_wheel/worlds
```

## Build Instructions
```bash
cd ~/ros2_ws
colcon build --packages-select two_wheel
source ~/.bashrc
```

## Launch Commands
```bash
# RViz only
ros2 launch two_wheel two_wheel_display.launch.py

# Gazebo only
ros2 launch two_wheel two_wheel_gazebo.launch.py

# Both RViz + Gazebo
ros2 launch two_wheel rviz_gazebo_combined.launch.py

# Control robot
ros2 run two_wheel robot_controller
```

## Future Plans
- Add 4-wheel drive robot variant
- Hardware deployment with physical robot
- Additional sensor integration

## License
Apache-2.0
