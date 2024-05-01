#! /usr/bin/env python

import rclpy
import rclpy.exceptions
from rclpy.node import Node
import cv2
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge, CvBridgeError
from .cvfpscalc import CvFpsCalc
from .gesturepredictor import *

QUEUE = 2
ros2_dir = "/home/dheeraj/unnon97/projects/ws_ros2"
model_keypointclassifier = ros2_dir + "/src/py_handgesture/py_handgesture/model/keypoint_classifier/keypoint_classifier.tflite"
label_keypointclassifier = ros2_dir + "/src/py_handgesture/py_handgesture/model/keypoint_classifier/keypoint_classifier_label.csv"
show_img = True

class HandSignRecognition(Node):
    def __init__(self, queue = QUEUE):
        """
        Creates a node for sign recognition
        """
        super().__init__('image_subscriber')
        self.img_subscriber = self.create_subscription(Image, '/webcam/camera', self.callback,10)
        self.gesture_publisher = self.create_publisher(String,'/gesture/handsign',queue)
        self.gesture_predictor = GestureRecognition(label_keypointclassifier,model_keypointclassifier)
        self.cv_fps_calc = CvFpsCalc(buffer_len=10)

    def callback(self, msg):
        """
        Callback Function for image subcriber
        """
        try:
            height = msg.height
            width = msg.width
            channel = msg.step//msg.width
            frame = np.reshape(msg.data, (height,width,channel))
            debug_img, gesture = self.gesture_predictor.recognize(frame)
            mssg = String()
            mssg.data = gesture
            self.gesture_publisher.publish(mssg)
            if show_img:
                fps = self.cv_fps_calc.get()
                debug_img = self.gesture_predictor.draw_fps_info(debug_img,fps)
                cv2.imshow("ROS2 Gesture Recognition",debug_img)
                cv2.waitKey(10)            
        except CvBridgeError as error:
            print(error)

def main(args=None):
    rclpy.init(args=args)
    try:
        hand_sign = HandSignRecognition()
        rclpy.spin(hand_sign)
    except rclpy.exceptions.ROSInterruptException:
        cv2.destroyAllWindows()
        rclpy.shutdown()

if __name__ == "__main__":
    main()