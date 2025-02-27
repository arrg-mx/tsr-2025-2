cmake_minimum_required(VERSION 3.8)
project(nodes_topics_pkg)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclpy REQUIRED) #for python scripts
find_package(std_msgs REQUIRED)

# Install Directories
install(
  DIRECTORY scripts
  DESTINATION share/${PROJECT_NAME}/
)

# Add cpp programs
add_executable(my_node_cpp src/my_node_cpp.cpp)
ament_target_dependencies(my_node_cpp rclcpp)

add_executable(number_pub_node_cpp src/number_pub_node_cpp.cpp)
ament_target_dependencies(number_pub_node_cpp rclcpp std_msgs)

add_executable(counter_node_cpp src/counter_node_cpp.cpp)
ament_target_dependencies(counter_node_cpp rclcpp std_msgs)

# Install targents in the package

install(TARGETS 
  my_node_cpp
  number_pub_node_cpp
  counter_node_cpp 
  DESTINATION lib/${PROJECT_NAME}
)

# Install Python modules
ament_python_install_package(${PROJECT_NAME})

#Install Python executables #They must start with the shebag tag
install(PROGRAMS
  scripts/my_node_py.py
  scripts/number_pub_node_py.py
  scripts/counter_node_py.py
  DESTINATION lib/${PROJECT_NAME} )

ament_package()
