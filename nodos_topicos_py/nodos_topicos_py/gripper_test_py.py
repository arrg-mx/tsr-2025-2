#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from builtin_interfaces.msg import Duration

import time
from math import cos, sin, acos, asin, atan2, sqrt

class GripperControlNode(Node):
    def __init__(self):
        super().__init__("gripper_control_node")
        topic_gripper_ = "/dofbot_gripper_controller/joint_trajectory"
        self.lamda_ = 0

        self.gripper_publisher_ = self.create_publisher(JointTrajectory, topic_gripper_, 10)
        self.gripper_joints_ = ['grip_joint', 'rfinger_joint_01', 'rfinger_joint_02', 'lfinger_grip_joint_01',
                                 'lfinger_grip_joint_02', 'lfinger_grip_joint_03']
        self.timer_ = self.create_timer(0.5, self.timer_callback)
        self.get_logger().info('Nodo de control del gripper dofbot en funcionamiento')

    def timer_callback(self):
        
        gripper_msg = JointTrajectory()
        gripper_msg.joint_names = self.gripper_joints_
        gripper_point = JointTrajectoryPoint()

        if self.lamda_ == 0:
            # Open gripper
            gstate = 1.57
            gripper_st = gripper_state(gstate)
            gripper_point.positions = gripper_st
            gripper_point._time_from_start = Duration(sec=2)
            gripper_msg.points.append(gripper_point)
            self.gripper_publisher_.publish(gripper_msg)
            self.get_logger().info('Gripper open')
            self.get_logger().info('poture {}'.format(gripper_st))
            time.sleep(10)
            self.lamda_ +=1

        elif self.lamda_ == 1:
            # Close gripper
            gstate_2 = 0
            gripper_st = gripper_state(gstate_2)
            gripper_point.positions = gripper_st
            gripper_point._time_from_start = Duration(sec=2)
            gripper_msg.points.append(gripper_point)
            self.gripper_publisher_.publish(gripper_msg)
            self.get_logger().info('Gripper close')
            self.get_logger().info('poture {}'.format(gripper_st))
            time.sleep(10)
            self.lamda_ +=1

        elif self.lamda_ == 2:
            # Open gripper
            gstate = 1.57
            gripper_st = gripper_state(gstate)
            gripper_point.positions = gripper_st
            gripper_point._time_from_start = Duration(sec=2)
            gripper_msg.points.append(gripper_point)
            self.gripper_publisher_.publish(gripper_msg)
            self.get_logger().info('Gripper open')
            self.get_logger().info('poture {}'.format(gripper_st))
            time.sleep(10)

def gripper_state(theta):
    
    return [float(-theta), float(theta), float(-theta), float(theta), float(-theta), float(theta)]


def main(args=None):
    rclpy.init(args=args)
    node = GripperControlNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()