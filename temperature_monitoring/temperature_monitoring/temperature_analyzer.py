import rclpy
from rclpy.node import Node
from interfaces.msg import TemperatureData

class TemperatureAnalyzer(Node):

    def __init__(self):
        super().__init__('temperature_analyzer')
        self.subscription = self.create_subscription(
            TemperatureData,
            'temperature_data',
            self.analyze_temperature,
            10)
        self.subscription  # prevent unused variable warning
        self.threshold = 25.0

    def analyze_temperature(self, msg):
        if msg.temperature > self.threshold:
            self.get_logger().warn(f'ATENCAO!!! ALTA TEMPERATURA: {msg.sensor_name} - {msg.temperature:.2f}')
        else:
            self.get_logger().info(f'Temperatura estável: {msg.sensor_name} - {msg.temperature:.2f}')

def main(args=None):
    rclpy.init(args=args)
    node = TemperatureAnalyzer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
