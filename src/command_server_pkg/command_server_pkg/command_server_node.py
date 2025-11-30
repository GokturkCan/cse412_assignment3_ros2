import rclpy
from rclpy.node import Node

from command_interfaces.srv import ComputeCommand

class CommandServer(Node):
    """Service node that classifies input as HIGH or LOW based on a threshold."""

    def __init__(self):
        super().__init__('command_server')

        # Create a service server for /compute_command
        self.srv = self.create_service(
            ComputeCommand,
            '/compute_command',
            self.handle_compute_command
        )

        self.get_logger().info('Command server is ready to receive requests.')

    def handle_compute_command(self, request, response):
        """Handle incoming service requests and set output to HIGH or LOW."""
        value = request.input

        if value > 10.0:
            response.output = "HIGH"
        else:
            response.output = "LOW"

        self.get_logger().info(f'Received: {value} -> Response: {response.output}')
        return response


def main(args=None):
    """Main entry point of the command server node."""
    rclpy.init(args=args)
    node = CommandServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
