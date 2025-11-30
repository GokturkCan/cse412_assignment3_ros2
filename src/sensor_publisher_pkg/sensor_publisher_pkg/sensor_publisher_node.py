import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class SensorPublisher(Node):
    """Simple sensor publisher that increments a counter and publishes it."""

    def __init__(self):
        super().__init__('sensor_publisher')

        # Create a publisher for /sensor_value topic
        self.publisher_ = self.create_publisher(Float32, '/sensor_value', 10)

        # Internal counter
        self.counter = 0.0

        # Create a timer that fires every 0.1 seconds
        self.timer = self.create_timer(0.1, self.timer_callback)

    def timer_callback(self):
        """Increment counter and publish it."""
        self.counter += 1.0  # Increment by 1.0

        msg = Float32()
        msg.data = float(self.counter)

        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')

def main(args=None):
    """Main entry point of the node."""
    rclpy.init(args=args)
    node = SensorPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
