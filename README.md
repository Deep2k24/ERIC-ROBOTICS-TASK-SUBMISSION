# testbed_navigation

## Overview
The `testbed_navigation` package implements navigation capabilities for the robot using the ROS 2 Navigation Stack. It includes configurations for localization, path planning, and control, enabling the robot to navigate autonomously in a simulated environment.

## Approach

### 1. Localization
- **AMCL (Adaptive Monte Carlo Localization)** is used for probabilistic localization of the robot within the map.
- The `amcl_params.yaml` file contains parameters for:
  - Particle filter settings.
  - Sensor model configurations.
  - Update frequencies for localization.

### 2. Path Planning
- The `planner_server.yaml` file configures the global planner to compute paths from the robot's current position to the goal.
- **Dijkstra's Algorithm** is used for pathfinding by setting `use_astar: false` in the `GridBased` plugin.

### 3. Path Following
- The `controller_server.yaml` file configures the local planner to follow the computed path while avoiding obstacles.
- The `RegulatedPurePursuitController` plugin is used for smooth and efficient path following.

### 4. Costmaps
- The package uses global and local costmaps to represent the environment:
  - **Global Costmap**: Represents the entire map for global planning.
  - **Local Costmap**: Represents the robot's immediate surroundings for obstacle avoidance.
- Costmap parameters are defined in the `planner_server.yaml` and `controller_server.yaml` files.

### 5. Launch Files
- **localization.launch.py**: Launches the AMCL node for localization.
- **map_loader.launch.py**: Loads the map for navigation.

## Challenges Faced
1. **Costmap Configuration**:
   - Ensuring the costmaps were correctly configured to handle dynamic obstacles and unknown spaces.
   - Debugging issues with costmap boundaries and inflation layers.

2. **Path Planning**:
   - Fine-tuning the planner parameters to balance path optimality and computation time.
   - Addressing issues with path feasibility in cluttered environments.

3. **Path Following**:
   - Tuning the `RegulatedPurePursuitController` parameters for smooth and accurate path following.
   - Handling edge cases where the robot deviated from the path due to sensor noise.

## Lessons Learned
- Proper configuration of costmaps is critical for reliable navigation.
- Tuning planner and controller parameters requires iterative testing in simulation.
- Modular design and clear documentation simplify debugging and future enhancements.

## How to Use

### 1. Build the Package
```bash
cd /home/deep/assignment_ws
colcon build --packages-select testbed_navigation
source install/setup.bash
```

### 2. Launch Localization
```bash
ros2 launch testbed_navigation localization.launch.py
```

### 3. Load the Map
```bash
ros2 launch testbed_navigation map_loader.launch.py
```

### 4. Send Navigation Goals
Use RViz or a ROS 2 action client to send navigation goals to the robot.

