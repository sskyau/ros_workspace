execute_process(COMMAND "/home/skyau/ros_workspace/build/gazebo_ros/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/skyau/ros_workspace/build/gazebo_ros/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
