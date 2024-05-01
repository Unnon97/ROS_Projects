#! /usr/bin/env python

import numpy as np
import cv2

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image

class ImgSubscriber(Node):
    def __init__(self):
        super().__init__('image_subscriber')
        self.subscription = self.create_subscription(Image, '/webcam/camera', self.listener_callback, 10)

    def listener_callback(self, msg):
        height = msg.height
        width = msg.width
        channel = msg.step//msg.width
        frame = np.reshape(msg.data, (height,width,channel))
        self.get_logger().info("Image Received")

        cv2.imwrite("Webcam.png",frame)

    
def main(args = None):
    rclpy.init(args=args)
    image_subscriber = ImgSubscriber()
    rclpy.spin(image_subscriber)
    rclpy.shutdown()


if __name__ == '__main__':
    main()

