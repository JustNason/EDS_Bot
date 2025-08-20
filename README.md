## EDS Robot

This is a GitHub repo containing the source code of my atonomous robotics project "EDS_Bot"

You can copy this file and replace all instances of `eds_bot` within the launcher files with the name of your robot. Alse ensure that when following this README.md replace any `eds_bot` with the name of your robot. EX: `ros2 launch eds_bot launch_robot.launch.py`, replace `eds_bot` with the name of your robot.

Note that each directory currently has at least one file in it to ensure that git tracks the files (and, consequently, that a fresh clone has direcctories present for CMake to find). These example files can be removed if required (and the directories can be removed if `CMakeLists.txt` is adjusted accordingly).