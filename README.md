<img width="635" height="450" alt="image" src="https://github.com/user-attachments/assets/60fb8c96-3380-423c-b7b4-9febf337c93f" />


# **SkyNet – Autonomous Drone System for Indoor Navigation, Object Detection & ArUco-Based Inventory Management (ROS2)**

### *Developed during International Internship – Avignon University, France (2024)*

---

## **📌 Overview**

**SkyNet** is an advanced autonomous drone ecosystem developed during an international research internship at **Avignon University, France**, under the guidance of leading researchers in IoT, Robotics, AI, and Cybersecurity.
The system integrates **Crazyflie 2.1** and **Tello EDU** drones to achieve:

* Autonomous indoor navigation
* Real-time SLAM (Simultaneous Localization and Mapping)
* Obstacle avoidance
* YOLOv8-based object & face detection
* PID-controlled object tracking
* ArUco marker–based warehouse inventory management

The project demonstrates the fusion of **robotics**, **computer vision**, **ROS2**, and **machine intelligence** to create a unified multi-drone autonomous platform.

---

## **📘 Table of Contents**

1. Introduction
2. Key Objectives
3. Features
4. System Architecture
5. Hardware Components
6. Software Stack
7. Methodology
8. Data Collection
9. Results
10. Findings & Discussions
11. Limitations
12. Future Enhancements
13. Business & Industry Impact
14. Project Schedule / Gantt
15. Installation & Setup (ROS2 + Drones)
16. References

---

## **1. Introduction**

SkyNet addresses modern industry needs for **autonomous warehouse operations**, **indoor navigation**, and **robotic perception** by deploying two specialized drones:

### **Crazyflie 2.1**

Used for mapping, SLAM, autonomous flight, and obstacle avoidance.

<img width="585" height="585" alt="image" src="https://github.com/user-attachments/assets/3a3e4d41-dcf6-40cc-85c1-7b7b9ce71b38" />


### **Tello EDU**

Used for image-based tasks such as YOLOv8 object detection, face recognition, and ArUco-based inventory scanning.

The unified ROS2-based architecture enables reliable, modular, and scalable autonomous drone operation.

<img width="550" height="429" alt="image" src="https://github.com/user-attachments/assets/b76f40ce-d474-4c7b-b705-a10da6cbb8a8" />


---

## **2. Key Objectives**

* Build an **autonomous indoor navigation system** using ROS2 SLAM Toolbox on Crazyflie 2.1.
* Implement **real-time object detection and face recognition** using YOLOv8 on Tello EDU.
* Develop **PID-controlled** object tracking for dynamic target following.
* Integrate **ArUco markers** for warehouse inventory identification & verification.
* Enable a **multi-drone coordinated architecture** with real-time telemetry and sensor fusion.

---

## **3. Key Features**

### **Crazyflie 2.1 – Autonomy Module**

* 2D SLAM map generation
* AMCL-based localization
* A* path planning
* 5-direction obstacle avoidance via Multiranger Deck
* Optical flow stabilization
* Autonomous waypoint navigation

### **Tello EDU – Vision Intelligence Module**

* YOLOv8 object detection (real-time)
* YOLOv8 face detection (fine-tuned)
* PID-based object following
* High-accuracy ArUco marker detection
* Automated inventory logging & anomaly detection

### **Unified ROS2 Ecosystem**

* Multi-node distributed system
* Real-time camera streaming with compressed image transport
* Scalable plug-and-play sensor architecture
* Live visualization in RViz2

---

## **4. System Architecture**

### **High-Level Design**

* ROS2 workstation acts as the command and compute hub
* Crazyflie communicates via Crazyradio PA
* Tello streams video via Wi-Fi UDP
* YOLO inference performed using OpenCV + ROS2 bridge
* ArUco module + inventory database for warehouse automation
* SLAM and Navigation Stack for map building and autonomous path execution

---

## **5. Hardware Components**

### **Crazyflie 2.1**

* Multiranger Deck (5× ToF sensors, 4m range)
* Flow Deck (optical flow + ToF for altitude)
* AI Deck (optional for on-board CV tasks)
* IMU (accelerometer, gyro, magnetometer)

### **Tello EDU**

* 5MP Camera
* Electronic Image Stabilization
* Programmable via SDK 2.0
* Wi-Fi video streaming
* Vision positioning system

---

## **6. Software Stack**

* **ROS2 Humble**
* **Crazyflie2 ROS packages**
* **OpenCV (ArUco + image processing)**
* **YOLOv8 (Ultralytics)**
* **PID Controller Module**
* **Navigation Stack 2**
* **SLAM Toolbox**
* **RoboFlow for dataset annotation**

---

## **7. Methodology**

### **Crazyflie – Autonomy Pipeline**

1. Firmware flashing & PID tuning
2. ROS2 integration
3. Sensor fusion from:

   * Multiranger
   * Flow Deck
   * IMU
4. 2D SLAM map creation
5. A* global planner
6. Dynamic obstacle avoidance
7. Autonomous execution of waypoints

### **Tello – Vision Pipeline**

1. Dataset creation & data augmentation
2. YOLOv8 training (COCO + custom face dataset)
3. Real-time compressed video streaming
4. Inference for bounding box + class prediction
5. PID velocity mapping
6. Target tracking
7. ArUco marker detection & database lookup

---

## **8. Data Collection**

* Sensor data (ranges, IMU, optical flow)
* Video datasets for object & face detection
* ArUco marker calibration set
* Checkerboard calibration images
* Autonomous flight telemetry logs
* SLAM maps for validation

---

## **9. Results**

### **Crazyflie**

* Map deviation < **5cm**
* Positional accuracy error: **3 cm** average
* 98% obstacle avoidance success rate
* Real-time SLAM + navigation stable at 30–40 Hz

### **Tello**

* YOLOv8 object detection AP: **85%**
* Face detection accuracy: **88%**
* PID tracking error: **<5 cm**
* ArUco detection accuracy: **95%**
* Inventory scan time reduced by **70%** vs. manual scans

---

## **10. Findings & Discussion**

* Small drones can achieve **research-grade** autonomous navigation indoors.
* YOLOv8 + Tello provides competitive accuracy despite compute limitations.
* ROS2 dramatically simplifies multi-drone orchestration.
* ArUco markers enable near error-free warehouse automation.
* Combining SLAM + CV + PID yields a robust holistic autonomy framework.

---

## **11. Limitations**

* Limited battery life (7–13 minutes)
* Crazyflie payload constraints
* Wi-Fi latency affecting Tello streaming
* Sensitivity to lighting for computer vision
* Limited compute on-board → reliance on off-board processing

---

## **12. Future Enhancements**

* Real-time **3D SLAM**
* Multi-drone swarm coordination
* GPU-based inference with on-board accelerators
* Integration of LiDAR / depth cameras
* Autonomous charging station
* RTS for industrial warehouse deployment

---

## **13. Business & Industry Impact**

### **Applicable to:**

* Warehouse automation
* Inventory audits
* Search & rescue
* Facility inspection
* Smart logistics
* Indoor mapping & surveillance

### **Outcomes**

* Improved accuracy
* Reduced auditing costs
* Faster operations
* Reduced human risk

---

## **14. Project Schedule – Gantt Summary**

<img width="1220" height="588" alt="image" src="https://github.com/user-attachments/assets/1c8a6f4c-7c8d-4fb5-ad0b-c7e0c9e095b2" />


---

## **15. Installation & Setup**

### **Prerequisites**

* ROS2 Humble
* Ubuntu 22.04
* Python 3.10
* OpenCV
* Ultralytics YOLOv8
* Crazyradio PA
* Tello EDU


---

## **16. References**

All 30+ references from IEEE, MDPI, ResearchGate, Diva Portal included.

---

