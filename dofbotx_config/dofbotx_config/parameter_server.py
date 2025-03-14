#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.parameter import Parameter
from rcl_interfaces.msg import ParameterDescriptor, SetParametersResult

class DofbotParamSrv(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        # Para declarar un parametro se utiliza 
        # el método 'declare_parameter'
        self.declare_parameter(
            name='time_period',
            value=0.01,
            descriptor=ParameterDescriptor(description="Este es un parametro")
        )
        # Para declarar un conjunto de parametros se utiliza 
        # el método 'declare_parameters'
        self.declare_parameters(
            namespace='',
            parameters=[
                ('lin_vel_max', 0.1),
                ('ang_vel', 0.04),
                ('pid_const', [0.2,10.2,4.34]),
                ('joint_names', rclpy.Parameter.Type.STRING_ARRAY),
                ('joint_vals', rclpy.Parameter.Type.DOUBLE_ARRAY),
                ('robot_ip', rclpy.Parameter.Type.STRING)
            ]
        )

        # Para leer un parametro se utiliza 
        # el método 'get_parameter'
        self.__time_period = self.get_parameter('time_period').get_parameter_value().double_value
        # Para validar un parametro antes de cambiar su valor
        # utilizamos una funcion asincrona asociada al evento
        # 'on_set_parameter'
        self.add_on_set_parameters_callback(self.__on_parameter_change)
        self.get_logger().info("Dofbot Parameter Server initialized.")

    def __on_parameter_change(self, params:list[Parameter]):
        success = True
        for param in params:
            if param.name == 'time_period':
                if param.value <= 0.0:
                    self.get_logger().warning(f"Parameter '{param.name}' no puede ser menor o igual a cero.")
                    success = False
            else:
                self.get_logger().info(f"Parameter '{param.name}': no es monitoreado.")

        result_msg = SetParametersResult()
        result_msg.successful = success
        result_msg.reason = "Por errores de tipo o valor"

        return result_msg    

def init_srv(args=None):
    rclpy.init(args=args)
    param_srv = DofbotParamSrv('dofbot_config')
    rclpy.spin(param_srv)
    rclpy.shutdown()

if __name__ == "__main__":
    init_srv()
