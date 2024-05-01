
import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='py_handgesture',
            namespace='signrecogniser',
            executable='recogniser',
            output='screen',
        ),
        Node(
            package='ros2_webcam',
            namespace='webcampublisher',
            executable='webcampub',
            output = 'screen'
        )
    ])