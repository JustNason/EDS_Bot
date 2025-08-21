import os

from ament_index_python.packages import get_package_share_directory


from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command
from launch.actions import RegisterEventHandler
from launch.event_handlers import OnProcessStart

from launch_ros.actions import Node



def generate_launch_description():


    # Include the robot_state_publisher launch file, provided by our own package. Force sim time to be enabled
    # !!! MAKE SURE YOU SET THE PACKAGE NAME CORRECTLY !!!

    package_name='eds_bot' #<--- CHANGE ME
    use_slam=True
    slam_mode=0

    joystick = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch','joystick.launch.py'
                )])
    )
    
    rviz2 = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        if use_slam
        {
            arguments=['-d', os.path.join(
            get_package_share_directory(package_name), 'config', 'map.rviz'
        )],
        }
        else
        {
            arguments=['-d', os.path.join(
            get_package_share_directory(package_name), 'config', 'main.rviz'
        )],
        }
        output='screen'
    )


    slam_params_file = os.path.join(
        get_package_share_directory(package_name),
        'config',
        'mapper_params_online_async.yaml'
    )

    slam = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('slam_toolbox'), 'launch', 'online_async_launch.py'
        )]),
        launch_arguments={
            'slam_params_file': slam_params_file,
            'use_sim_time': 'false'
            ''
        }.items()
    )


    return LaunchDescription([
        joystick,
        rviz2,
        if use_slam
        {
            slam
        }

    ])
