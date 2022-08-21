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

客户端可以订阅频道.
发布者 发布消息到频道

```

## 订阅
subscribe channel1


#发布消息去 test
publish channel1 test

```

## Jedis 操作redis

### 引入依赖

```xml
  
  <dependency>
    <groupId>redis.client</groupId>
    <artifactId>jedis</artifactId>
    <version>3.2.0</version>
  </dependency>

```
### 常见操作

### 整合到SpringBoot



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