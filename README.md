## Thesis Project

! [Photo 4] (images/photo4.png)

This project implements an autonomous RC car using ROS 2 (Humble), combining simulation, perception, and navigation into a complete robotic system. The vehicle is modeled with an Ackermann steering system and equipped with a LiDAR sensor for environment perception.

The system is simulated in Gazebo, where realistic physics and sensor data are generated, and visualized in RViz for real-time monitoring of LiDAR data, TF frames, and mapping results. Using SLAM Toolbox, the robot builds a 2D map of its environment while estimating its position.

The project demonstrates a full autonomous robotics pipeline:

Simulation → LiDAR Perception → SLAM → Mapping → Navigation (Nav2)

This work serves as a foundation for scalable autonomous driving systems and showcases the integration of robotics and AI techniques in a controlled environment.

