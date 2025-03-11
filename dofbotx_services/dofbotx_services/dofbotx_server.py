#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from dofbotx_interfaces.srv import GetStatus

class  DofbotX_Server(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self.__status_server = self.create_service(
            GetStatus, 
            '/dofbotx_status',
            self._on_status_clbk
            )
        self.get_logger().info(f"{node_name} server initialized.")
        

    def _on_status_clbk(self, request:GetStatus.Request, response:GetStatus.Response):        
        self.get_logger().info("Recibi una peticion")
        is_active = request.is_dofbotx_active
        if is_active:
            response.is_active = True
        else:
            response.is_active = False

        response.success = True
        response.string_status_message = "dofbotx_status executed successfully"

        return response
            
def main(args=None):
    rclpy.init(args=args)
    dofbot_server_node = DofbotX_Server("dofbotx_server_node")
    rclpy.spin(dofbot_server_node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()