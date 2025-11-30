#!/bin/bash
set -e

# Source ROS 2 Humble environment
source /opt/ros/humble/setup.bash

# Source workspace overlay (built inside the container)
source /ws/install/setup.bash

# Launch the project (using the launch file in /ws/launch)
ros2 launch /ws/launch/my_project.launch.py
