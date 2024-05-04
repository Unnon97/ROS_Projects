#ifndef KALMAN_FILTER_HPP
#define KALMAN_FILTER_HPP


#include <Eigen/Dense>

class KalmanFilter {
    private:
        Eigen::VectorXd x_; // State vector
        Eigen::MatrixXd P_; // State covariance matrix
        Eigen::MatrixXd F_; // State transition matrix
        Eigen::MatrixXd Q_; // Process noise covariance matrix
        Eigen::MatrixXd H_; // Measurement matrix
        Eigen::MatrixXd R_; // Measurement noise covariance matrix
    public:
        KalmanFilter();

        void predict(const Eigen::VectorXd& u);
        void update(const Eigen::VectorXd& z);
        const Eigen::VectorXd& getState() const;
};

#endif