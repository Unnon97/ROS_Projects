#ifndef KALMAN_FILTER_NODE_HPP
#define KALMAN_FILTER_NODE_HPP

#include "rclcpp/rclcpp.hpp"
#include "sensor_msgs/msg/imu.hpp"
#include "cpp_kalmanfilter/kalman_filter.hpp"

class KalmanFilterNode: public rclcpp::Node {
    private:
        void imu_callback(const sensor_msgs::msg::Imu::SharedPtr msg);

        rclcpp::Subscription<sensor_msgs::msg::Imu>::SharedPtr imu_sub_;
        rclcpp::Publisher<sensor_msgs::msg::Imu>::SharedPtr filtered_imu_pub_;

        KalmanFilter kf_;
    public:
        KalmanFilterNode();
};


#endif