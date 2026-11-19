import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

PARTS = ['rover', 'mission']   # later: 'ekf', 'slam', 'nav', 'explore', 'detector', ...


def generate_launch_description():
    rover_launch = os.path.join(
        get_package_share_directory('rover_bringup'), 'launch', 'rover.launch.py')

    args = [DeclareLaunchArgument(p, default_value='true') for p in PARTS]

    return LaunchDescription(args + [
        # The whole hardware layer from your ugv-rover repo
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(rover_launch),
            condition=IfCondition(LaunchConfiguration('rover'))),

        Node(package='inspection_mission', executable='mission_manager',
             name='mission_manager', output='screen',
             condition=IfCondition(LaunchConfiguration('mission'))),
    ])