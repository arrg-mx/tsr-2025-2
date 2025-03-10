#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class RobotPubNode(Node):

    def __init__(self):
        super().__init__("robot_pub_node")

        self.robot_name_ = "Robot_1"
        self.publisher_ = self.create_publisher(String, "robot_topic_pub", 10)
        self.timer_ = self.create_timer(0.5, self.publis_info)
        self.get_logger().info("Nodo robot_pub_node esta activo")
        

    def publis_info(self):
        msg = String()
        msg.data = "Hola soy el robot" + str(self.robot_name_) + " desde robot_pub_node"
        self.publisher_.publish(msg)
        


def main(args=None):
    rclpy.init(args=args)
    node = RobotPubNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()