import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.actions import RegisterEventHandler
from launch.event_handlers import OnProcessStart
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():

    package_name = 'eds_bot'

    # --- robot_state_publisher ---
    rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory(package_name),'launch','rsp.launch.py'
        )]),
        launch_arguments={'use_sim_time': 'false', 'use_ros2_control': 'true'}.items()
    )

    # --- twist_mux ---
    twist_mux_params = os.path.join(get_package_share_directory(package_name),'config','twist_mux.yaml')
    twist_mux = Node(
        package="twist_mux",
        executable="twist_mux",
        parameters=[twist_mux_params],
        remappings=[('/cmd_vel_out','/diff_cont/cmd_vel_unstamped')]
    )

    # --- robot_description directly from URDF ---
    urdf_file = os.path.join(get_package_share_directory(package_name), 'description', 'robot.urdf.xacro')
    with open(urdf_file, 'r') as infp:
        robot_description = {'robot_description': infp.read()}

    # --- controller manager ---
    controller_params_file = os.path.join(get_package_share_directory(package_name),'config','my_controllers.yaml')
    controller_manager = Node(
        package="controller_manager",
        executable="ros2_control_node",
        parameters=[robot_description, controller_params_file]
    )
    delayed_controller_manager = TimerAction(period=5.0, actions=[controller_manager])

    # --- spawners ---
    diff_drive_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["diff_cont"],
    )
    joint_broad_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_broad"],
    )

    # --- Ensure spawners start only after controller_manager ---
    delayed_diff_drive_spawner = RegisterEventHandler(
        event_handler=OnProcessStart(
            target_action=controller_manager,
            on_start=[diff_drive_spawner],
        )
    )
    delayed_joint_broad_spawner = RegisterEventHandler(
        event_handler=OnProcessStart(
            target_action=controller_manager,
            on_start=[joint_broad_spawner],
        )
    )

    # --- LiDAR ---
    lidar_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory(package_name),'launch','ld19lidar.launch.py'
        )])
    )
    delayed_lidar = RegisterEventHandler(
        event_handler=OnProcessStart(
            target_action=diff_drive_spawner,
            on_start=[lidar_launch]
        )
    )

    # --- Return LaunchDescription ---
    return LaunchDescription([
        rsp,
        twist_mux,
        delayed_controller_manager,
        delayed_diff_drive_spawner,
        delayed_joint_broad_spawner,
        delayed_lidar
    ])
