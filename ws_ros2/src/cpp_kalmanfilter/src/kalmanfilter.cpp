#include "cpp_kalmanfilter/kalman_filter.hpp"

KalmanFilter::KalmanFilter() {
    x_ = Eigen::VectorXd::Zero(6); //Initializing state vector to zeros
    P_ = Eigen::MatrixXd::Identity(6,6); // Initializing state covariance matrix as identity
    F_ = Eigen::MatrixXd::Identity(6,6); // Assuming identity matrix initially
    Q_ = Eigen::MatrixXd::Identity(6,6);
    H_ = Eigen::MatrixXd::Identity(6,6);
    R_ = Eigen::MatrixXd::Identity(6,6);
}

void KalmanFilter::predict(const Eigen::VectorXd &u) {
    x_ = F_* x_ + u;
    P_ = F_* P_ * F_.transpose() + Q_;

}

void KalmanFilter::update(const Eigen::VectorXd &z) {
    Eigen::VectorXd y = z - H_ * x_;
    Eigen::MatrixXd S = H_ * P_ * H_.transpose() + R_;
    Eigen::MatrixXd K = P_ * H_.transpose() * S.inverse();

    x_ = x_ + K * y;
    P_ = (Eigen::MatrixXd::Identity(P_.rows(), P_.cols()) - K * H_) * P_;
}

const Eigen::VectorXd& KalmanFilter::getState() const {
    return x_;
}