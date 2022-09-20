## 内存模型
## 类加载机制

javap -c 
## JVM 调优
减少 stop the world

堆的样子

eden|Old |S0 | S1

计算一个对象的大小


minor gc 
## 垃圾收集器
Parallel Scavenge 默认使用的
Serial
G1
ZGC
ParNew
asfasdf
## 垃圾收集算法
 标记清除算法

## 一些工具
Jmap Jstack Jinfo athera

## JVM什么是调优？
1.根据需求进行VM规划和预调优
2.优化运行VM运行环境（慢，卡顿）（怎么才能定位一个系统的瓶颈？压测)1
3.解次VM运行过程中出现的各种问题( Memory Leak ooM)
### 调优，从规划开始
•调优，从业务场景开始，没有业务场景的调优都是耍流氓
•无监控（压力测试，能看到结果），不调优
•步骤：
    1.熟悉业务场景（没有最好的垃圾回收器，只有最合适的垃圾回收器)
        1.响应时间，停顿时间 (CMS G1 ZGC)（需要给用户作响成)
        2.吞吐员 =用户时间(用户时间+ GC时间)PsT
    2.选择回收器组合
    3. 计算内存需求（经验值 1.5G 16G)
    4. 选定CPU（越高越好）
    5. 设定年代大小，升级年龄
    6.设定日志参数
        1.-x10ggc:/opt/x××/1g5/××x-xxx-gc-9t.1og-xx:+UseGCLogFileRotation -xx:NumberofGCLogFiles=5•
        xx:GCLogFileSize=20M -xx:+PrintGcDetails-xx:+PrintGCDatestamps-xx:+PrintGCCause
        2.或者每天产生一个日志文件
    7.观察日志情况
    * 案例1: 垂直电商，最高每日百万订单，处理订单系统需要什么样的服务器配胃？
    这个问题比较业余，因为很多不同的服务器配首都能支撑(1.5G 16G) 1小时360000生中时间段，100个订单/秒,(找一小时内的高峰期，1000订单/秒）