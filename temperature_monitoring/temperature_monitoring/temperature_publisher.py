import rclpy
from rclpy.node import Node
from interfaces.msg import TemperatureData
import random

class TemperaturePublisher(Node):

    def __init__(self):
        super().__init__('temperature_publisher')
        self.publisher_ = self.create_publisher(TemperatureData, 'temperature_data', 10)
        self.timer = self.create_timer(1.0, self.publish_temperature)
        self.sensor_name = "Sensor1"

    def publish_temperature(self):
        msg = TemperatureData()
        msg.sensor_name = self.sensor_name
        msg.temperature = random.uniform(20.0, 30.0)
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg.sensor_name} - {msg.temperature:.2f}')

def main(args=None):
    rclpy.init(args=args)
    node = TemperaturePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
