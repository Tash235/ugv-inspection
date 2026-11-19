# ugv-inspection
Autonomous reconnaissance and inspection stack for the Waveshare UGV Rover (Jetson Orin Nano, ROS 2 Humble).
Depends on the hardware layer in `ugv-rover` (`rover_base`, `rover_bringup`, `rover_description`).

## Packages
| Package | Purpose |
|---|---|
| inspection_interfaces | InspectedObject msgs + GetObjects srv |
| inspection_bringup | Top-level launch + configs |
| inspection_perception | Detection + object localisation |
| inspection_mission | Mission manager + object registry |
| inspection_report | Post-mission report generator |

## Build
    cd ~/rover_ws && colcon build --symlink-install --packages-up-to inspection_bringup
    source install/setup.bash

## Run
    ros2 launch inspection_bringup inspection.launch.py            # everything
    ros2 launch inspection_bringup inspection.launch.py rover:=false   # no hardware