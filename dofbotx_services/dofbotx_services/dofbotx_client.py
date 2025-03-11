#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from dofbotx_interfaces.srv import GetStatus


class DofbotXClient(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self.__status_client = self.create_client(
            GetStatus,
            '/dofbotx_status'
        )
        self.get_logger().info("Waiting for service...")
        self.__wait_count = 3
        while not self.__status_client.wait_for_service(timeout_sec=1.0):
            if self.__wait_count == 0:
                self.get_logger().warning("Service not available for 3 secs. Bye.")
                return 1
            self.get_logger().info(f"Waiting for service {self.__wait_count} secs...")
            self.__wait_count = self.__wait_count -1

    def call_service(self, is_active: bool):
        peticion = GetStatus.Request()
        peticion.is_dofbotx_active = is_active
        self.future = self.__status_client.call_async(peticion)
        rclpy.spin_until_future_complete(self,future=self.future)

        return self.future.result()


def main(args=None):
    rclpy.init(args=args)
    dofbot_client = DofbotXClient('dofbot_client_node')
    resultado = dofbot_client.call_service(True)
    print(f"Resultado de la llamada: {resultado.is_active}")
    print(f"Resultado del proceso: {resultado.success}")
    print(f"Mensaje del proceso: {resultado.string_status_message}")
    rclpy.shutdown()

if __name__ == "__main__":
    main()