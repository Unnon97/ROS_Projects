#include "rclcpp/rclcpp.hpp"
#include "cpp_kalmanfilter/kalmanfilternode.hpp"

int main(int argc, char** argv) {
    rclcpp::init(argc, argv);
    auto node = std::make_shared<KalmanFilterNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}