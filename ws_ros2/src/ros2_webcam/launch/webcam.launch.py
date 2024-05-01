
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ros2_webcam',
            namespace='webcampublisher',
            executable='webcampub',
            output = 'screen'
        ),
        Node(
            package='ros2_webcam',
            namespace='webcamsubscriber',
            executable='webcamsub',
            output = 'screen'
        )
    ])