# CSE412 - Robotics  
## Assignment 3: ROS2 Nodes, Services and Docker Deployment  
### Student: Göktürk Can (230611501)  
### Date: 2025-11-30

---

## 📌 1. Overview

This repository contains the complete implementation of **Assignment 3** for the CSE412 Robotics course.  
The project demonstrates:

- ROS2 Humble workspace setup  
- Custom service (srv) package  
- Three ROS2 Python nodes  
- A launch file that starts all nodes together  
- Full Dockerization (build + run)  
- Verification inside a running container  
- SSF_SHA256 verification script (required by the assignment)

---

## 📁 2. Repository Structure

cse412_assignment3_ros2/
│
├── src/
│   ├── sensor_publisher_pkg/
│   ├── data_processor_pkg/
│   ├── command_server_pkg/
│   └── command_interfaces/
│       └── srv/
│           └── ComputeCommand.srv
│
├── launch/
│   └── my_project.launch.py
│
├── Dockerfile
├── entrypoint.sh
├── SSF_HASH.txt
└── README.md


---
