import rclpy
from rclpy.node import Node
from interfaces.msg import RobotPosition
import random

class Robot1(Node):

    def __init__(self):
        super().__init__('robot_1')
        self.publisher_ = self.create_publisher(RobotPosition, 'robot_1/position', 10)
        self.subscription_2 = self.create_subscription(RobotPosition, 'robot_2/position', self.listener_callback, 10)
        self.subscription_3 = self.create_subscription(RobotPosition, 'robot_3/position', self.listener_callback, 10)
        self.timer = self.create_timer(1.0, self.publish_position)
        self.robot_name = "robot_1"

    def publish_position(self):
        msg = RobotPosition()
        msg.robot_name = self.robot_name
        msg.x = random.uniform(0.0, 10.0)
        msg.y = random.uniform(0.0, 10.0)
        msg.theta = random.uniform(-3.14, 3.14)
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg.robot_name} - x: {msg.x:.2f}, y: {msg.y:.2f}, theta: {msg.theta:.2f}')

    def listener_callback(self, msg):
        self.get_logger().info(f'Received from {msg.robot_name}: x: {msg.x:.2f}, y: {msg.y:.2f}, theta: {msg.theta:.2f}')

def main(args=None):
    rclpy.init(args=args)
    node = Robot1()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
