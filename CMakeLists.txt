cmake_minimum_required(VERSION 2.8.3)
project(yourpackagename)
#set(CMAKE_CXX_STANDARD 11)
#set(CMAKE_CXX_STANDARD_REQUIRED ON)


#find_package(Armadillo REQUIRED)
#include_directories(${ARMADILLO_INCLUDE_DIRS})
#find_package(OpenCV REQUIRED)
find_package(OpenMP REQUIRED)
if(OPENMP_FOUND)
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${OpenMP_C_FLAGS}")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${OpenMP_CXX_FLAGS}")
set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} ${OpenMP_EXE_LINKER_FLAGS}")
endif()
#include_directories(${ARMADILLO_INCLUDE_DIRS} ${OpenCV_INCLUDE_DIRS} ${OpenMP_INCLUDE_DIRS})

add_definitions(-std=c++14)

find_package(catkin REQUIRED COMPONENTS roscpp std_msgs geometry_msgs visualization_msgs genmsg message_generation
  actionlib
  sensor_msgs
  control_msgs
  trajectory_msgs
  cv_bridge
  dynamic_reconfigure
  intera_core_msgs
  intera_motion_msgs
  intera_interface
  )
  
  find_package(FRI REQUIRED COMPONENTS
    kuka_fri
)


add_message_files(FILES custommessagetype.msg)

generate_messages(DEPENDENCIES std_msgs geometry_msgs)

catkin_package(
   # INCLUDE_DIRS include
   CATKIN_DEPENDS roscpp std_msgs geometry_msgs genmsg visualization_msgs message_runtime
  actionlib
  sensor_msgs
  control_msgs
  trajectory_msgs
  cv_bridge
  dynamic_reconfigure
  intera_core_msgs
  intera_motion_msgs
  intera_interface
)

include_directories(include
  ${catkin_INCLUDE_DIRS}
)
add_executable(example1 src/example1.cpp)
add_dependencies(example1 ${catkin_EXPORTED_TARGETS})
target_link_libraries(example1 ${catkin_LIBRARIES} armadillo)

add_executable(example2 src/example2.cpp)
add_dependencies(example2 ${catkin_EXPORTED_TARGETS})
target_link_libraries(example2 ${catkin_LIBRARIES} armadillo ${OpenCV_LIBS} ${OpenMP_LIBS})



