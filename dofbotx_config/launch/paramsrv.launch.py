#!/usr/bin/env python3

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    id = LaunchDescription()

    paramsrv_node = Node(
        package='dofbotx_config',
        executable='param_srv',
    )

    # Acciones a ejecutar en el momento de lanzar 
    # los procesos descritos en este 'launch'
    # script
    # 1.
    id.add_action(paramsrv_node)

    return id