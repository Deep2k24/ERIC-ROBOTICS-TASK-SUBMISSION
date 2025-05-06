from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    use_sim_time_arg = DeclareLaunchArgument(
            "use_sim_time",
            default_value="true"
    )

    map_name_arg = DeclareLaunchArgument(
            "map_name",
            default_value="testbed_map" 
    )

    map_name = LaunchConfiguration("map_name")
    use_sim_time = LaunchConfiguration("use_sim_time") 

    lifecycle_nodes = ["map_server"]

    map_path = PathJoinSubstitution([
        get_package_share_directory("testbed_bringup"),
        "maps",
        map_name,
        "testbed_world.yaml"
    ])

    Nav2_map_server = Node(
        package = "nav2_map_server",
        executable = "map_server",
        output = "screen",
        parameters = [
            {"yaml_filename": map_path},
            {"use_sim_time" : use_sim_time}
        ]    
    )

    

    nav2_lifecycle_manager = Node(
        package="nav2_lifecycle_manager",
        executable="lifecycle_manager",
        name="lifecycle_manager_map_server",
        output="screen",
        parameters=[
            {"node_names": lifecycle_nodes},
            {"use_sim_time": use_sim_time},
            {"autostart": True}
        ]
    )

    return LaunchDescription([
        use_sim_time_arg,
        map_name_arg,
        Nav2_map_server,
        nav2_lifecycle_manager
    ])
