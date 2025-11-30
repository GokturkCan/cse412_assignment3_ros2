import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class DataProcessor(Node):
    """Subscribes to /sensor_value, processes it, and publishes on /processed_value."""

    def __init__(self):
        super().__init__('data_processor')

        # Create subscription to /sensor_value
        self.subscription = self.create_subscription(
            Float32,
            '/sensor_value',
            self.listener_callback,
            10
        )

        # Create publisher for /processed_value
        self.publisher_ = self.create_publisher(Float32, '/processed_value', 10)

    def listener_callback(self, msg):
        """Process the incoming sensor value by multiplying by 2."""
        input_value = msg.data
        processed_value = input_value * 2.0

        out_msg = Float32()
        out_msg.data = float(processed_value)

        self.publisher_.publish(out_msg)
        self.get_logger().info(f'Received: {input_value} -> Processed: {processed_value}')

def main(args=None):
    """Main entry point of the node."""
    rclpy.init(args=args)
    node = DataProcessor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

