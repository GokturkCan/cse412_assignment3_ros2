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

```text
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
```

❗ Excluded from the repo as required
```text
    build/
    install/
    log/
```

## 🚀 3. Node Descriptions

### 1️⃣ `sensor_publisher_pkg`
* **Description:** Publishes a continuously increasing floating-point value.
* **Topic:** `/sensor_value`
* **Frequency:** Every 0.1 seconds (10 Hz)
* **Message Type:** `std_msgs/msg/Float32`

### 2️⃣ `data_processor_pkg`
* **Description:** Subscribes to sensor data, processes it, and republishes.
* **Subscribes to:** `/sensor_value`
* **Logic:** Multiplies incoming data by `2.0`
* **Publishes on:** `/processed_value`

### 3️⃣ `command_server_pkg`
* **Description:** Provides a computation service based on threshold logic.
* **Service:** `/compute_command`
* **Service Type:** `command_interfaces/srv/ComputeCommand`
* **Logic:**
  * If input `> 10` → Returns **"HIGH"**
  * Else → Returns **"LOW"**

## 🧩 4. Launch Dosyası

### `launch/my_project.launch.py`

Bu launch dosyası, tüm üç node'u (düğümü) eş zamanlı olarak başlatmak için kullanılır.

```python
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package='sensor_publisher_pkg', executable='sensor_publisher', output='screen'),
        Node(package='data_processor_pkg', executable='data_processor', output='screen'),
        Node(package='command_server_pkg', executable='command_server', output='screen'),
    ])
```

## 🐳 5. Docker Instructions

These steps assume you have Docker installed and are executing the commands from the root directory of the repository where the `Dockerfile` is located.

### 5.1 Build the Docker Image

Build the ROS application image and tag it as **myrosapp**:

```bash
docker build -t myrosapp .
```
###5.2 Run the Container

```bash
docker run --rm myrosapp
```

This automatically launches:

```bash
ros2 launch my_project my_project.launch.py
```

inside the container (via entrypoint.sh).


## 🧪 6. Verification Commands (Inside Container)

Open a second terminal:

```bash
docker ps
docker exec -it <container_id> bash
```

Then run:

### 6.1 Topic List

```bash
ros2 topic list
```

Expected:

```bash
/sensor_value
/processed_value
/compute_command/_service_event
/rosout
```

### 6.2 Echo processed output

```bash
ros2 topic echo /processed_value
```
Expected stream:

```bash
data: 2.0
data: 4.0
data: 6.0
...
```

### 6.3 Service Call

```bash
ros2 service call /compute_command command_interfaces/srv/ComputeCommand "{input: 12.5}"
```

Expected:

```bash
output: "HIGH"
```

## 🔐 7. SSF Verification

The assignment requires generating a SHA256-based verification file using ssf.sh.
The generated hash is stored in:

```bash
SSF_HASH.txt
```

This file is included in the repository as required.

## 🎥 8. Video Link

The full demonstration video (YouTube – Unlisted):

➡️ https://youtu.be/-DnoEN-U7mU

- Video includes:

- SSF script execution

- Docker image build

- Docker container run

- Topic list + echo + service call verification

## ✅ 9. Conclusion

This assignment demonstrates a complete ROS2 and Docker workflow:

- Modular node design

- Custom service creation

- Multi-node launch system

- Fully portable Docker environment

- Successful topic/service verification

All components operate correctly both on the host and inside Docker, fulfilling the entire assignment specification.

## 📎 10. Contact

If needed, you can reach me at:

- Göktürk Can
  
- gokturk.can@istun.edu.tr

- gokturkcan404@gmail.com

- 230611501

- Istanbul Health and Technology University

