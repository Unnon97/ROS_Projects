import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():
    bag_file_path = "/home/dheeraj/unnon97/projects/ws_ros2/src/cpp_kalmanfilter/data/smb_navigation/smb_navigation.db3"

    return LaunchDescription([
        ExecuteProcess(
            cmd=['ros2', 'bag', 'play', '--loop', bag_file_path],
            output='screen'
        ),
        Node(
            package='cpp_kalmanfilter',
            executable='kf_exec',
            name='kalman_filter_node',
            output='screen'
        ),
    ])