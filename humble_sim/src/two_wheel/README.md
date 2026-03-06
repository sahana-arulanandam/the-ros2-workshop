# Two-Wheel Differential Drive Robot

A ROS2 Humble package for simulating a two-wheel differential drive robot with lidar in Gazebo and RViz.

## Quick Start

### Installation

```bash
cd ~/ros2_ws/src
git clone https://github.com/yourusername/urdf_gazebo.git
cd ~/ros2_ws
colcon build --packages-select two_wheel
source install/setup.bash
```

### Environment Setup

Add to `~/.bashrc`:
```bash
source /opt/ros/humble/setup.bash
source /usr/share/gazebo/setup.bash
source $HOME/ros2_ws/install/setup.bash
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:$HOME/ros2_ws/install/two_wheel/share/two_wheel
export GAZEBO_RESOURCE_PATH=$GAZEBO_RESOURCE_PATH:$HOME/ros2_ws/install/two_wheel/share/two_wheel/worlds
```

Then run: `source ~/.bashrc`

## Usage

### Launch Simulation

**RViz only:**
```bash
ros2 launch two_wheel two_wheel_display.launch.py
```

**Gazebo only:**
```bash
ros2 launch two_wheel two_wheel_gazebo.launch.py
```

**RViz + Gazebo:**
```bash
ros2 launch two_wheel rviz_gazebo_combined.launch.py
```

### Control the Robot

**Option 1: Custom Keyboard Controller**

In a new terminal:
```bash
ros2 run two_wheel robot_controller
```

**Controls:**
- `w` - Forward
- `s` - Backward
- `a` - Left
- `d` - Right
- `x` - Stop
- `q` - Quit

**Option 2: ROS2 Default Teleop**

Alternatively, use the standard ROS2 teleop twist keyboard:
```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

## Project Details

For detailed project structure, specifications, and future plans, see [PROJECT_CONTEXT.md](PROJECT_CONTEXT.md)

## License

Apache-2.0
