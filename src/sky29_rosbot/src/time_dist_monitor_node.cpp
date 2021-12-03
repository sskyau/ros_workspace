#include <ros/ros.h>
#include <rosgraph_msgs/Clock.h>
#include <nav_msgs/Odometry.h>
#include <cmath>
#include <message_filters/subscriber.h>
#include <message_filters/time_synchronizer.h>


ros::Time simTime;
float dist;
float old_x;
float old_y;

bool isFirstRun = true;

float new_x;
float new_y;


void myCallback (const rosgraph_msgs::Clock::ConstPtr &msg)
{
    simTime = msg->clock;
    //std::cout << "SimTime: " << msg->clock << std::endl;
}

void odom_callback (const nav_msgs::Odometry::ConstPtr &msg)
{
    if (isFirstRun){
        old_x = round(msg->pose.pose.position.x*100.0)/100.0;
        old_y = round(msg->pose.pose.position.y*100.0)/100.0;
    }

    new_x = round(msg->pose.pose.position.x*100.0)/100.0;
    new_y = round(msg->pose.pose.position.y*100.0)/100.0;
    
    std::cout << "old x: " << old_x << " old y: " << old_y << std::endl;
    std::cout << "new x: " << new_x << " new_y: " << new_y << std::endl;

    dist = dist + sqrt(pow((new_x - old_x),2) + pow((new_y - old_y),2));
    old_x = new_x;
    old_y = new_y;
    isFirstRun = false;

} 


/*
void callback(const  rosgraph_msgs::Clock::ConstPtr &clk_msg, const nav_msgs::Odometry::ConstPtr &odom_msg){
    if (isFirstRun){
        old_x = round(odom_msg->pose.pose.position.x*1000.0)/1000.0;
        old_y = round(odom_msg->pose.pose.position.y*1000.0)/1000,0;
    }

    simTime = clk_msg->clock;
    new_x = round(odom_msg->pose.pose.position.x*1000.0)/1000.0;
    new_y = round(odom_msg->pose.pose.position.y*1000.0)/1000.0;
    dist = dist + sqrt(pow((new_x - old_x),2) + pow((new_y - old_y), 2));
    old_x = new_x;
    old_y = new_y;
    isFirstRun = false;
}
*/

int main (int argc, char **argv)
{
    ros::init(argc, argv, "time_dist_monitor_node");
    ros::NodeHandle n("~");
    ros::Subscriber clock_sub = n.subscribe("/clock", 10, myCallback);
    ros::Subscriber odom_sub = n.subscribe("/odom", 10, odom_callback);
     
    //message_filters::Subscriber<rosgraph_msgs::Clock> clock_sub(n, "/clock", 1);
    //message_filters::Subscriber<nav_msgs::Odometry> odom_sub(n, "/odom", 1);
    //message_filters::TimeSynchronizer <rosgraph_msgs::Clock, nav_msgs::Odometry> sync(clock_sub, odom_sub, 1);
    //sync.registerCallback(boost::bind(&callback, _1, _2));

    ros::Rate loop_rate(50);

    int counter = 25;
    while (ros::ok())
    {
        ++counter;
        ros::spinOnce();
        loop_rate.sleep();
        if (counter > 49)
        {
            counter = 0;
            std::cout << "Simulation Time: " << simTime << " Cumulative distance travelled: " << dist << std::endl;
        }
    }

}
