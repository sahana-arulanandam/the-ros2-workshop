from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    publisher_node = Node(
        package='pub_sub',
        executable='number_publisher',
        name='number_publisher',
        output='screen'
    )

    subscriber_node = Node(
        package='pub_sub',
        executable='number_subscriber',
        name='number_subscriber',
        output='screen'
    )

    return LaunchDescription([
        publisher_node,
        subscriber_node
    ])
