# Base image as requested
FROM ros:humble-ros-base

# Use bash for RUN commands
SHELL ["/bin/bash", "-c"]

# Create and use workspace directory
WORKDIR /ws

# Copy source code and launch/entrypoint files into the container
COPY src /ws/src
COPY launch /ws/launch
COPY entrypoint.sh /ws/entrypoint.sh

# Install colcon and build tools (if not already in the base image)
RUN apt-get update && apt-get install -y \
    python3-colcon-common-extensions \
    && rm -rf /var/lib/apt/lists/* \
    && source /opt/ros/humble/setup.bash \
    && colcon build

# Make sure entrypoint is executable
RUN chmod +x /ws/entrypoint.sh

# Run the entrypoint when the container starts
ENTRYPOINT ["/ws/entrypoint.sh"]
