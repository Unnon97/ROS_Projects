#! /usr/bin/env python

import os
import rclpy
from rclpy.node import Node
import numpy as np

import cv2
from sensor_msgs.msg import Image
import json
from ament_index_python.packages import get_package_share_directory

TOPIC = '/webcam/camera'
QUEUE_SIZE = 1
PERIOD = 0.1

class CameraPublisher(Node):
    def __init__(self, capture, topic = TOPIC, queue = QUEUE_SIZE, period = PERIOD):
        '''Initialise the camera publisher class'''
        super().__init__('camera_publisher')
        timer_period = period
        self.time = self.create_timer(timer_period, self.timer_callback)
        self.publisher_ = self.create_publisher(Image, topic, queue)

        self.capture = capture
        self.i = 0

    def timer_callback(self):
        """
        Timer callback function which captures images 
        and publishes them to ros2 topic TOPIC
        """
        if self.capture.isOpened():

            #read image date
            ret, frame = self.capture.read()

            #preprocess image data and convert to ros 2 message
            msg = Image()
            msg.header.stamp = Node.get_clock(self).now().to_msg()
            msg.header.frame_id = 'Webcam'
            msg.height = np.shape(frame)[0]
            msg.width = np.shape(frame)[1]
            msg.encoding = "bgr8"
            msg.is_bigendian = False
            msg.step = np.shape(frame)[2] * np.shape(frame)[1]
            msg.data = np.array(frame).tobytes()

            #publish message
            self.publisher_.publish(msg)
            # self.get_logger().info('%d Images Published' % self.i)

        #image counter increment
        self.i += 1

        return None

def main(args = None):

    settings = os.path.join(get_package_share_directory('ros2_webcam'), "settings.json")

    with open(settings) as fp:
        content = json.load(fp)

        #create OpenCV Videocapture object
        capture = cv2.VideoCapture(content["device_index"])
        capture.set(cv2.CAP_PROP_BUFFERSIZE, 2)
        #initialize node and start publishing
        rclpy.init(args=args)
        camera_publisher = CameraPublisher(capture, content["topic"], content["queue_size"],content["period"])

        rclpy.spin(camera_publisher)

        #shuts the node down and releases everything
        camera_publisher.destroy_node()
        rclpy.shutdown()
        capture.release()

    return None

if __name__ == '__main__':
    main()
    