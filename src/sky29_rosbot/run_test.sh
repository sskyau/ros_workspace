#!/bin/bash

cd ~/ros_workspace/src/rosbot_bath
source ~/ros_workspace/devel/setup.sh

for lidar in {2..1..0.5}
    do
    for ir in {0.7..0.6..0.05}
        do
        for orient in {0.95..0.8..0.05}
            do  
            konsole --hold --new-tab&
            konsole --hold --new-tab -e $SHELL -c "roslaunch rosbot_bath rosbot_bath.launch"&
            konsole --hold --new-tab -e $SHELL -c "roslaunch sky29_rosbot sky29_rosbot.launch lidar_thres:=$LIDAR ir_thres:=$IR orient_thres:=$ORIENT"

            done
        done
    done
