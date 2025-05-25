#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from builtin_interfaces.msg import Duration

import time
from math import cos, sin, acos, asin, atan2, sqrt

class DofbotControlNode(Node):
    def __init__(self):
        super().__init__("dofbot_tray_control_node")
        self.lamda_ = 0
        topic_dofbot_ = "/dofbot_trajectory_controller/joint_trajectory"
        self.dofbot_publisher_ = self.create_publisher(JointTrajectory, topic_dofbot_, 10)
        self.dofbot_joints_ = ['arm_joint_01', 'arm_joint_02', 'arm_joint_03', 'arm_joint_04', 'arm_joint_05']
        self.timer_ = self.create_timer(0.5, self.timer_callback)
        self.get_logger().info('Nodo de control del dofbot en funcionamiento')

    def timer_callback(self):
        dofbot_msg = JointTrajectory()
        dofbot_msg.joint_names = self.dofbot_joints_
        dofbot_point = JointTrajectoryPoint()

        if self.lamda_ == 0:
            x_1 = 0.2
            y_1 = 0.0
            z_1 = 0.05
            theta_p_1 = 3.1416*(3/4)
            theta_g_1 = 0.0
            solution_pos = dofbot_ink(x_1, y_1, z_1, theta_p_1, theta_g_1)
            dofbot_point.positions = solution_pos
            dofbot_point.time_from_start = Duration(sec=2)
            dofbot_msg.points.append(dofbot_point)
            self.dofbot_publisher_.publish(dofbot_msg)
            self.get_logger().info('poture {}'.format(solution_pos))
            time.sleep(15)
            self.lamda_ += 1

        elif self.lamda_ == 1:
            x_2 = 0.05
            y_2 = -0.15
            z_2 = 0.11
            theta_p_2 = 3.1416*(3/4)
            theta_g_2 = 0 
            solution_pos = dofbot_ink(x_2, y_2, z_2, theta_p_2, theta_g_2)
            dofbot_point.positions = solution_pos
            dofbot_point.time_from_start = Duration(sec=2)
            dofbot_msg.points.append(dofbot_point)
            self.dofbot_publisher_.publish(dofbot_msg)
            self.get_logger().info('poture {}'.format(solution_pos))
            time.sleep(15)
            self.lamda_ += 1

        elif self.lamda_ == 2:
            # punto de deposicion del objeto 
            x_3 = 0.15
            y_3 = 0.15
            z_3 = 0.10
            theta_p_3 = 3.1416*(3/4) 
            theta_g_3 = 0 
            solution_pos = dofbot_ink(x_3, y_3, z_3, theta_p_3, theta_g_3)
            dofbot_point.positions = solution_pos
            dofbot_point.time_from_start = Duration(sec=2)
            dofbot_msg.points.append(dofbot_point)
            self.dofbot_publisher_.publish(dofbot_msg)
            self.get_logger().info('poture {}'.format(solution_pos))
            time.sleep(15)
            self.lamda_ += 1

        elif self.lamda_ == 3:
            solution_pos = [ float(0.0), float(0.0), float(0.0), float(0.0), float(0.0)]
            dofbot_point.positions = solution_pos
            dofbot_point.time_from_start = Duration(sec=2)
            dofbot_msg.points.append(dofbot_point)
            self.dofbot_publisher_.publish(dofbot_msg)
            self.get_logger().info('poture {}'.format(solution_pos))
            time.sleep(10)

def dofbot_ink(x_P, y_P, z_P, theta_1_P, theta_g):
    # Parametros
    z_0_1 = 0.105
    L_1 = 0.084
    L_2 = 0.084
    L_3 = 0.115

    theta_1 = atan2(y_P, x_P)
    aux_x = sqrt(pow(x_P, 2) + pow(y_P, 2)) - L_3*sin(theta_1_P)
    aux_z = z_P - z_0_1 -L_3*cos(theta_1_P)
    norm_4_P = sqrt(pow(aux_z, 2)+pow(aux_x, 2))
    epsilon = acos(aux_z/norm_4_P)
    alpha = acos((pow(L_1, 2)+pow(norm_4_P, 2)-pow(L_2, 2))/(2*L_1*norm_4_P))
    theta_2 = epsilon - alpha
    theta_3 = 3.1416 - asin((sin(alpha)*sqrt(pow(aux_x, 2) + pow(aux_z, 2)))/(L_2))
    theta_4 = theta_1_P - theta_2 - theta_3
    theta_5 = theta_g
    return [ float(theta_1), float(-theta_2), float(-theta_3), float(-theta_4), float(theta_5)]


def main(args=None):
    rclpy.init(args=args)
    node = DofbotControlNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()