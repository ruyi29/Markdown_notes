# ROS2/C++ 自定义消息类型
https://blog.csdn.net/moriarty_jack/article/details/110846337

__首先注意一点，在ROS 2 dashing发行版里面，只有C++的功能包可以自定义消息类型；也就是说，在创建包的时候，只有选择 ament_cmake方式创建的包才可以自定义消息，但是python类型的功能包可以导入由C++类型包创建的自定义消息。__

### 1.创建自定义消息功能包
- 进入工作空间
```
cd ~/ros_ws/src
```
- 创建功能包
```
ros2 pkg create --build-type ament_cmake test_msgs
```
由于这个功能包只是生成自定义消息类型，所以我一般都是不在这里添加任何算法，所以这个包里面也没有可执行文件，因此不需要指定节点名字。

### 2.创建msg文件
```
cd test_msgs
mkdir msg
cd msg
gedit TestMsg.msg
```
TestMsg.msg文件内容如下：
```
float32[] x
float32[] y 
```
**注意事项：**

1. TestMsg.msg：文件名一定要以大写开头；
2. 文件中的变量一定全部都要小写，不能有大写出现；同时也不要出现特殊符号
3. 在C++调用该头文件时候，会以下划线区分大写，例如上面的文件编译得到后，在c++调用时如下：
```
#include “test_msgs/msg/test_msg.hpp”
```

4. vector的定义是在数据类型后面增加一个方括号[ ]
5. 可以用自己定义的数据类型作为变量的数据类型，例如在另一个msg文件中定义这样的一个变量：
```
TestMsg position
```
### 3,修改CMakelists文件
在find_package(ament_cmake REQUIRED)下面添加：
```
find_package(builtin_interfaces REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(std_msgs REQUIRED)

set(msg_files
  "msg/TestMsg.msg"
)
rosidl_generate_interfaces(${PROJECT_NAME} ${msg_files} DEPENDENCIES builtin_interfaces geometry_msgs std_msgs ADD_LINTER_TESTS)

ament_export_dependencies(rosidl_default_generators)
ament_export_dependencies(rosidl_default_runtime)
ament_export_include_directories(include)
```
### 4,修改package文件
由于接口依赖rosidl_default_generators来生成特定于语言的代码，因此需要声明对其的依赖。
在 <buildtool_depend>ament_cmake</buildtool_depend>下面添加：
```
<build_depend>rosidl_default_generators</build_depend>

<exec_depend>rosidl_default_runtime</exec_depend>

<member_of_group>rosidl_interface_packages</member_of_group>
```

### 5.编译&查看消息
```
cd ../../..
# 编译
colcon build --packages-select test_msgs
# 添加环境
source install/setup.bash
# 查看msg数据
ros2 interface show test_msgs/msg/TestMsg
```
可以在终端看到我们定义的消息类型

## 6.调用
### Python调用
在package.xml里添加
```
<exec_depend>test_msgs</exec_depend>
```
在源文件里添加
```
from test_msgs.msg import TestMsg
```
使用的时候
```
msg = TestMsg()
msg.x.append(1.0) // 加入msg里有signal这个消息
```
### C++调用
在CMakeLists.txt里面添加
```
find_package(test_msgs REQUIRED) # 根据你的名称修改
ament_target_dependencies(${PROJECT_NAME}_node std_msgs rclcpp test_msgs)
```
在package.xml里面添加
```
<depend>test_msgs</depend>
```
在源文件中包含
(特别注意，这里的格式，消息文件是驼峰风格的命名方式，也就是通过大写分割单词，但是包含的时候要用下划线风格，全部是小写)
```
#include "test_msgs/msg/test_msg.hpp" 
```
使用的时候
```
publisher = this->create_publisher<test::msg::MyOwnNum>("test", 10);
```