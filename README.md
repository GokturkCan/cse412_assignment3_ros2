\# CSE412 - Robotics ## Assignment 3: ROS2 Nodes, Services and Docker Deployment 
### Student: Göktürk Can (230611501) 
### Date: 2025-11-30

\---## 📌 1. Overview

This repository contains the complete implementation of \*\*Assignment 3\*\* for the CSE412 Robotics course.

The project demonstrates:- ROS2 Humble workspace setup - Custom service (srv) package - Three ROS2 Python nodes - A launch file that starts all nodes together - Full Dockerization (build + run) - Verification inside a running container - SSF\_SHA256 verification script (required by the assignment)

\---

\## 📁 2. Repository Structure

cse412\_assignment3\_ros2/

│

├── src/

│ ├── sensor\_publisher\_pkg/

│ ├── data\_processor\_pkg/

│ ├── command\_server\_pkg/

│ ├── command\_interfaces/ <-- Custom srv package

│ │ └── srv/ComputeCommand.srv

│

├── launch/

│ └── my\_project.launch.py

│

├── Dockerfile

├── entrypoint.sh

├── SSF\_HASH.txt

└── README.md

❗ Excluded from the repo as required: \`build/\`, \`install/\`, \`log/\`

\---## 🚀 3. Node Descriptions### \*\*1️⃣ sensor\_publisher\_pkg\*\*- Publishes a continuously increasing floating-point value on \`/sensor\_value\`- Publishes every \*\*0.1 seconds\*\*- Message type: \`std\_msgs/msg/Float32\`### \*\*2️⃣ data\_processor\_pkg\*\*- Subscribes to \`/sensor\_value\`- Multiplies incoming data by \*\*2.0\*\*- Publishes result on \`/processed\_value\`### \*\*3️⃣ command\_server\_pkg\*\*- Provides a service \`/compute\_command\`- Service type: \`command\_interfaces/srv/ComputeCommand\`- Logic: - If input > 10 → \`"HIGH"\` - Else → \`"LOW"\`

\---## 🧩 4. Launch File\`launch/my\_project.launch.py\` starts all three nodes simultaneously:\`\`\`python

from launch import LaunchDescription

from launch\_ros.actions import Node

def generate\_launch\_description():

return LaunchDescription(\[

Node(package='sensor\_publisher\_pkg', executable='sensor\_publisher', output='screen'),

Node(package='data\_processor\_pkg', executable='data\_processor', output='screen'),

Node(package='command\_server\_pkg', executable='command\_server', output='screen'),

\])

🐳 5. Docker Instructions

5.1 Build the Docker Image

docker build -t myrosapp .

5.2 Run the Container

docker run --rm myrosapp

This automatically launches:

ros2 launch my\_project my\_project.launch.py

inside the container (via entrypoint.sh).

🧪 6. Verification Commands (Inside Container)

Open a second terminal:

docker ps

docker exec -it bash

Then run:

6.1 Topic List

ros2 topic list

Expected:

/sensor\_value

/processed\_value

/compute\_command/\_service\_event

/rosout

6.2 Echo processed output

ros2 topic echo /processed\_value

Expected stream:

data: 2.0data: 4.0data: 6.0

...

6.3 Service Call

ros2 service call /compute\_command command\_interfaces/srv/ComputeCommand "{input: 12.5}"

Expected:

output: "HIGH"

🔐 7. SSF Verification

The assignment requires generating a SHA256-based verification file using ssf.sh.

The generated hash is stored in:

SSF\_HASH.txt

This file is included in the repository as required.

🎥 8. Video Link

The full demonstration video (YouTube – Unlisted):

➡️ https://youtu.be/-DnoEN-U7mU

Video includes:

SSF script execution

Docker image build

Docker container run

Topic list + echo + service call verification

✅ 9. Conclusion

This assignment demonstrates a complete ROS2 and Docker workflow:

Modular node design

Custom service creation

Multi-node launch system

Fully portable Docker environment

Successful topic/service verification

All components operate correctly both on the host and inside Docker, fulfilling the entire assignment specification.

