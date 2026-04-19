import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():

    package_name = 'maqui_na'

    world_arg = DeclareLaunchArgument(
        'world', default_value='', description='Path to world file'
    )
    spawn_robot_arg = DeclareLaunchArgument(
        'spawn_robot', default_value='true',
        description='Spawn robot from robot_description. Use false for worlds that already contain my_bot.'
    )

    rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory(package_name), 'launch', 'rsp.launch.py'
        )]),
        launch_arguments={'use_sim_time': 'true'}.items()
    )

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py'
        )]),
        launch_arguments={'world': LaunchConfiguration('world')}.items()
    )

    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-topic', 'robot_description',
            '-entity', 'my_bot',
        ],
        additional_env={'PATH': '/usr/bin:' + os.environ.get('PATH', '')},
        condition=IfCondition(LaunchConfiguration('spawn_robot')),
        output='screen'
    )

    return LaunchDescription([world_arg, spawn_robot_arg, rsp, gazebo, spawn_entity])
