#include "cpp_kalmanfilter/kalmanfilternode.hpp"

KalmanFilterNode::KalmanFilterNode() : Node("kf_exec") {
    imu_sub_ = this->create_subscription<sensor_msgs::msg::Imu>(
        "/imu/data", 10, std::bind(&KalmanFilterNode::imu_callback, this, std::placeholders::_1));
    filtered_imu_pub_ = this->create_publisher<sensor_msgs::msg::Imu>("/filtered/imu",10);
}

void KalmanFilterNode::imu_callback(const sensor_msgs::msg::Imu::SharedPtr msg) {
    Eigen::VectorXd measurement(6);
    measurement << msg->linear_acceleration.x,
                    msg->linear_acceleration.y,
                    msg->linear_acceleration.z,
                    msg->angular_velocity.x,
                    msg->angular_velocity.y,
                    msg->angular_velocity.z;

    kf_.predict(Eigen::VectorXd::Zero(6));
    kf_.update(measurement);

    auto filtered_msg = std::make_shared<sensor_msgs::msg::Imu>();
    filtered_msg->linear_acceleration.x = kf_.getState()[0];
    filtered_msg->linear_acceleration.y = kf_.getState()[1];
    filtered_msg->linear_acceleration.z = kf_.getState()[2];
    filtered_msg->angular_velocity.x = kf_.getState()[3];
    filtered_msg->angular_velocity.y = kf_.getState()[4];
    filtered_msg->angular_velocity.z = kf_.getState()[5];

    filtered_imu_pub_->publish(*filtered_msg);
}

