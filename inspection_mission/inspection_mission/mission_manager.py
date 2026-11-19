#!/usr/bin/env python3
"""mission_manager: Phase 1 placeholder. Publishes an empty object list at 1 Hz."""
import rclpy
from rclpy.node import Node

from inspection_interfaces.msg import InspectedObjectArray


class MissionManager(Node):
    def __init__(self):
        super().__init__('mission_manager')
        self.pub = self.create_publisher(InspectedObjectArray, 'inspection/objects', 10)
        self.create_timer(1.0, self.on_timer)
        self.get_logger().info('mission_manager up (Phase 1 placeholder)')

    def on_timer(self):
        msg = InspectedObjectArray()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'map'
        self.pub.publish(msg)          # empty list for now


def main():
    rclpy.init()
    node = MissionManager()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()