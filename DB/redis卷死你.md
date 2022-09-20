# Redis
## 安装
[官网](https://redis.io/)  
[中文网](http://www.redis.cn/)
官网上寻找一些文档就可以完成安装

[Redis 常用命令](https://redis.io/commands/)

## 支持的数据类型
1. String
2. List
3. set
4. ZSet
5. Hash

默认是16 个数据库 0-15

redis单线程 + 加多路复用
## 基本命令

1. key 操作

```shell

exists key

keys *

type key 查看key的类型
del key  删除指定的key数据
unlink key // 根据value 选择非阻塞删除,异步的删除

expire key //设置key的过期时间

ttl key  // -1 永不过期 , -2表示已经过期 ,表示过期时间.

msetnx

getrange name 0 3 //获取范围

setrange name 0 3  // 在那个范围内设置

setex // 设置过期时间
```
2. String 操作

```shell
get <key>

setnx <key><value>  只有key 不存在时,才会设置
incr<key>


decr<key>


```
3. List 操作

单建多值, 底层是一个双向链表


```shell
lpush/rpush    从左边 or 右边插入

lpop/rpop

lrange key start stop
lrange k1 0 -1 // 所有的

llen k1 // 获取长度

linsert key befor/after
lrem key  n //删除 n 个
lset //讲列表改成 set

```

zset 中跳表
https://zhuanlan.zhihu.com/p/361417273
https://segmentfault.com/a/1190000013418471

## 数据类型 Bitmap ,HyperLoglog, Geospatial
### Bitmap
setBit

getBit key

bitcount // 统计字符串被设置为1 的
### HyperLoglog
常遇到统计网站访问量, 可以使用redis中的 incr,incrby 轻松实现,但是如果像UV(UniqueVisitor,独立访客),独立IP,搜索记录数等需要去重复和计数

常见的方法: 
1) 利用mysql 中表的,使用distinct count 计算不重复
2) redis 提供了hash,set,bitmap等数据结构.
弊端是随着数据量不断增加,导致占用空间越来越大,对于非常大的数据集不切实际

HyperLoglog 利用很少空间计算出,数据集中不重复元素的个数

### 命令

```shell
## 添加指定元素到 HyperLoglog
pfadd <key> <element>[element...]

## 统计
pfcout <key>

## 合并
pfmerge <key1><key2>

```
### Geospatial
redis 中增加了对 GEO(地理信息), 经纬度2维坐标,提供了常见的设置,查询,范围查询,距离查询,经纬度HASH等操作
### 命令

```shell
## 添加指定元素到 HyperLoglog
geoadd<key><longitude><latitude><member>

geoadd china:city 121.47 31.23 shanghai 
geoadd china:city 121.47 31.23 shanghai 106.50 29.53 chongqing

## 获取上海坐标
geoops china:city shanghai

## 获得两个位置的直线距离
geodist <key> <member1>member2> [m|km|ft(英尺)|mi(英里)]

geodist china:city beijing shanghai km 

## 方圆几公里内的
georadius <key> <longitude><latitude> radius [m|km|ft(英尺)|mi(英里)]

```


## Redis的发布和订阅
redis  发布订阅(pub/sub) 是一种消息通信模式: 发布者(pub) 发送消息,订阅者(sub)接收消息

客户端可以订阅频道.发布者 发布消息到频道

```

## 订阅
subscribe channel1

#发布消息去 test
publish channel1 test

```

## Jedis操作redis

### 引入依赖

```xml
  
  <dependency>
    <groupId>redis.client</groupId>
    <artifactId>jedis</artifactId>
    <version>3.2.0</version>
  </dependency>

```
### 常见操作

```java
  
  public static void redisDemo(){
      Jedis jedis = new Jedis("127.0.0.1", 6379);
      Set set = jedis.keys("*");
      set.forEach(o -> System.out.println(o));
      List list = jedis.lrange("k1",0 ,-1);
      System.out.println(list);
      jedis.close();
  }

```

### 整合到SpringBoot

### Redies 中的事务
每个事务有隔离性 
* Multi
* Exec
* discard
组队, 执行,discard 放弃组队

组队时 可能错误
执行时 可能错误
#### 事务冲突的问题
并发的情况下回出现问题
解决的方案:
* 悲观锁

* 乐观锁
  使用方法
  whach[key] 
  unwhach 

## Redis 持久化
### RDB
在指定的时间间隔内将数据数据写入,磁盘
新建 子线程 fork

采用了linux 写时复制

config file 中的 SNAPSHOTTING 相关的配置

```
# 文件名字
dbfilename dump.rdb
#当前路径
dir ./
```

### AOF
append only file,以日志的形式记录下来写操作.
默认没有开启

启动路径在配置文件 redis.conf 中, 默认为 appendonly.aof

如果遇到异常, 可以通过 
```shell
redis-check-aof --fix appendonly.aof
```
配置同步频率

appendfsync always
appendfsync everysec  
appendfsync no


## 主从复制

实现读写分离,数据备份

### 搭建
编写不同端口的启动文件的config文件 

```shell
pidfile /var/run/redis_6379.pib
port 6379
dbfilename dump6379.db
log  ./6379_log_file.log
```

查看redis 状态
```shell
# 进入 redis
redis-cli -p 6379

#输入
info replication

##在从机上输入
slave of <ip><port>

```
### 一主多从

### 哨兵模式
哨兵模式是指若是主服务挂了, 会选择一个从服务,让从服务变成主服务

选择的策略


创建文件 sentinel.conf
```shell
# sentinel monitor mymaster <ip><port>  nums
# num 表示需要多少个从节点同意
sentinel monitor mymaster 127.0.0.1 6379  1
```
## 集群搭建
[Scaling with Redis Cluster](https://redis.io/docs/manual/scaling/)
[集群搭建](http://www.redis.cn/topics/cluster-tutorial.html)

## 应用问题
### 缓存穿透
1. 应用服务器压力变大了
2. redis 查询命中率低
3. 一直在查询 mysql

可能是有人在攻击,常见的解决方案

### 缓存击穿
1. 数据库访问压力瞬间变大
2. redis 里面没有出现大量key过期
3. redis 正常运行
   
某个key 过期,大量访问这个key
解决方法:
  预设一些key
### 缓存雪崩
极少时间内大量key 过期了
解决方法:

### 分布式锁

基于Redis 的分布式锁 

设置锁: setnx

释放锁: del







2.redis面试吊打面试官秘籍
3.redis的value类型
4.Redis在秒杀场景的应用
5.IO threads
 计算机系统的IO
   同步IO
   异步IO
   区别是: 数据由程序自己从内核拷贝回来,然后处理的是同步模型
   异步没有copy的过程


6.Redis如何使用
7.Redis雪崩，穿透，击穿，预热
8.数据库一致性&AOF持久化机制
9.Redis挂掉怎么办？
10.Redis角度看待架构设计
11.什么是锁？锁升级过程解析
12.单机锁分布式锁技术选型
13.Redis集群解决单点故障问题
14.CAP定理
15.客户端挂了怎么办？
16.Redis应用场景
17.说一下在你项目中的redis的应用场景
18.redis是单线程还是多线程
19.redis存在线程安全的问题么
20.遇到过缓存穿透么
21.遇到过缓存击穿么
22.如何避免缓存雪崩
23.缓存课后解答
24.redis是怎么删除过期key的(缓存时如何回收的)
25.缓存是如何淘汰的
26.如何进行缓存预热
27.数据库与缓存不一致如何解决
28.简述一下主从不一致的问题
29.描述一下redis持久化的方式
30.描述一下持久化原理
31.为什么使用setnx(redis实现分布式锁的指令)



wc775812
50684haha


https://github.com/CorentinJ/Real-Time-Voice-Cloning 就是拿来用哈哈

Pr0tectamsuser
All0wdpxuser