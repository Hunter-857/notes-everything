# ROS
ROS 系统介绍
ROS 设计的特点
1.点对点的设计
    点对点通信
2.多语言支持
3.架构 精简,集成度高
4.组件化工具包丰富
  3D可视化--rviz
  物理仿真 -- gazebo
  数据记录工具 -- rosbag
  Qt工具箱 --- rqt_*
5.免费且开源
[Tutorials](https://docs.ros.org/en/galactic/Tutorials.html)
## 
三个层次
开源社区
    文件系统
        计算图

计算图:
 节点(Node) --- 软件模块化
 节点管理器(ROS Master) 
 话题(Topic) 
 服务(Service)

 话题模型(发布/订阅) 
 kafuka类似

 服务模型(请求应答模型)

## ROS 文件系统
1.功能包清单
2.元功能包
3.功能包清单
4.信息类型
5.服务类型
6.代码
## ROS 开源社区
1.发行版
2.软件源
3.ROS wiki
4.邮件列表
5.ROS answer :咨询提问的网站
6.Blog (http://www.ros.org/news)

## 通过ROS的软件源安装
默认安装路径 /opt/ros

## ROS常用命令
catkin_create_pk
rqt_plot
rqt_graph
rospack
rostopic
rossevice list

## ROS 例子
小海龟仿真器

 一个终端: roscore
 一个终端: rosrun tutlesim tutlesim_node
 一个终端: rosrun tutlesim tutlesim_teleop_key





资料
ROS wiki : http://wiki.ros.org
ROS answer http://answer.ros.org
exbot 易科机器人实验室 : http://blog.exbot.net
古月居 www.guyuhome.com
ROSCon
