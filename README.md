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
1. A PC running Ubuntu 24.04 LTS (You can dual boot with Windows or you can use a VM. Please note that from my experience VMs seem to have issues especially on Apple silicon Macs.)
2. ROS2 Jazzy installed and working (Install it for [Ubuntu (deb packages)](https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html))
3. Install Gazebo and the following dependencies:

_Gazebo + ROS2 Bridge:_
```
sudo apt update && sudo apt upgrade
sudo apt install ros-jazzy-ros-gz
sudo apt install ros-gz-ros2-control
```

_ROS2 Dependencies:_
```
sudo apt install ros-jazzy-twist-mux
sudo apt install ros-jazzy-twist-stamper
sudo apt install ros-jazzy-ros2-control
sudo apt install ros-jazzy-ros2-controllers
```

Great! Now we can begin setting up our development workspace.
First, we create our `dev_ws` and `src` folders. Then, we clone our code into the `src` folder.
```
mkdir -p dev_ws/src
cd dev_ws/src

git clone https://github.com/JustNason/EDS_Bot.git
```
Now we build our workspace from source using colcon (If you don't have colcon installed, you can install it with `sudo apt install colcon`)
```
cd ~/dev_ws

source install/setup.bash
colcon build --symlink-install
```
