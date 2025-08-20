## EDS Robot

This is a GitHub repo containing the source code of my atonomous robotics project "EDS_Bot"

You can copy this repo and replace all instances of `eds_bot` within the launcher files with the name of your robot. Alse ensure that while following this README.md you replace eds_bot to the name of your robot when referencing the package. 
**EX:** `ros2 launch eds_bot launch_robot.launch.py`, replace `eds_bot` with the name of your robot.

This repository was created from _Josh Newans'_ [articubot_one](https://github.com/joshnewans/articubot_one), a very special thanks to him.
You can find his amazing ROS2 tutorials here:
[Articulated Robotics](https://www.youtube.com/@ArticulatedRobotics)

Installation
============
### Setting Up the Development Mechine

Before starting, ensure you have these things:
1. A PC running Ubuntu 24.04 LTS (You can dual boot with Windows or you can use a VM. Please not that from my experience VM seem to have issues especially on Apple silicon Macs.)
2. ROS2 Jazzy installed and working (Install it for [Ubuntu (deb packages)](https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html))
3. Install Gazebo and the following dependencies:
Gazebo + ROS2 Bridge:
```
sudo apt update && sudo apt upgrade
sudo apt install ros-jazzy-ros-gz
sudo apt install ros-gz-ros2-control
```

```
mkdir -p dev_ws/src
cd dev_ws/src

git clone https://github.com/JustNason/EDS_Bot.git
```
