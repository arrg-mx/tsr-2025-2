#!/usr/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class RobotState(Node):
    def __init__(self):
        super().__init__('robot_node')
        self._topico = self.create_publisher(String, '/topico', 10)
        self._timer_pub = self.create_timer(5, self.cuenta)
        self._contador = 0
        self.get_logger().info("El nodo ya fonuncia.")

    def cuenta(self):
        mensaje = String()
        self._contador += 1
        mensaje.data = f"Contando... {self._contador}"
        self._topico.publish(mensaje)

def main():
    rclpy.init()
    robot_node = RobotState()
    rclpy.spin(robot_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()