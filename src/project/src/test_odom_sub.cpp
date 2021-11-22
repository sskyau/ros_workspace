#include <ros/ros.h>
#include <nav_msgs/Odometry.h>

double pose_x;
double pose_y;
double pose_z;
double orient_x;
double orient_y;
double orient_z;
double orient_w;
double vel_linear;
double vel_angular;


void callback(const nav_msgs::Odometry::ConstPtr & msg)


{
    pose_x = msg->pose.pose.position.x;
    pose_y = msg->pose.pose.position.y;
    pose_z = msg->pose.pose.position.z;
    orient_x = msg->pose.pose.orientation.x;
    orient_y = msg->pose.pose.orientation.y;
    orient_z = msg->pose.pose.orientation.z;
    orient_w = msg->pose.pose.orientation.w;
    vel_linear = msg->twist.twist.linear.x;
    vel_angular = msg->twist.twist.angular.z;

}
int main (int argc, char **argv) 
{
    ros::init(argc, argv, "odom_listener");
    ros::NodeHandle n;
    ros::Subscriber sub = n.subscribe("/odom",1000, callback);
    ros::Rate loop_rate(50);    

    int counter = 25;
    while (ros::ok){
         ++counter;
         ros::spinOnce();
         loop_rate.sleep();
         std::cout << "Position: x: " << pose_x << " y: " << pose_y << " z: " << pose_z << std::endl;
         std::cout << "Orientation x: "<< orient_x << " y: " << orient_y << " z: " <<orient_z << std::endl;
         std::cout << "Velocity linear:" << vel_linear << " angular: " << vel_angular << std::endl; 
    }
    return 0;
}
    

