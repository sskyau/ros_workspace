# CMake generated Testfile for 
# Source directory: /home/skyau/ros_workspace/src/resource_retriever/test
# Build directory: /home/skyau/ros_workspace/build/resource_retriever/test
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(_ctest_resource_retriever_gtest_resource_retriever_utest "/home/skyau/ros_workspace/build/catkin_generated/env_cached.sh" "/usr/bin/python2" "/opt/ros/melodic/share/catkin/cmake/test/run_tests.py" "/home/skyau/ros_workspace/build/test_results/resource_retriever/gtest-resource_retriever_utest.xml" "--return-code" "/home/skyau/ros_workspace/devel/lib/resource_retriever/resource_retriever_utest --gtest_output=xml:/home/skyau/ros_workspace/build/test_results/resource_retriever/gtest-resource_retriever_utest.xml")
add_test(_ctest_resource_retriever_nosetests_test.py "/home/skyau/ros_workspace/build/catkin_generated/env_cached.sh" "/usr/bin/python2" "/opt/ros/melodic/share/catkin/cmake/test/run_tests.py" "/home/skyau/ros_workspace/build/test_results/resource_retriever/nosetests-test.py.xml" "--return-code" "\"/usr/bin/cmake\" -E make_directory /home/skyau/ros_workspace/build/test_results/resource_retriever" "/usr/bin/nosetests-2.7 -P --process-timeout=60 /home/skyau/ros_workspace/src/resource_retriever/test/test.py --with-xunit --xunit-file=/home/skyau/ros_workspace/build/test_results/resource_retriever/nosetests-test.py.xml")
