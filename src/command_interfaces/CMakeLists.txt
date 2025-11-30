cmake_minimum_required(VERSION 3.8)
project(command_interfaces)

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)

# Generate the service interface from srv/ComputeCommand.srv
rosidl_generate_interfaces(${PROJECT_NAME}
  "srv/ComputeCommand.srv"
)

ament_export_dependencies(rosidl_default_runtime)

ament_package()
