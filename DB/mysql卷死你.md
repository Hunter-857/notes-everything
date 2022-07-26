## 索引

### 为什么要用索引

加速, 查的太慢了

### mysql索引的基本原理

数据结构:
     二叉树
     哈希表
     红黑树(二叉平衡数)
     BTree
     B+Tree
各种数据结构的优缺点

```js
//innodb 索引页大小 大约16KB
SHOW CLOBAL STATUS like ‘innodb_page_size’

```

索引最左原则

### mysql聚簇索引和非聚簇索引的区别?

数据和索引放在同一个文件夹下就是 聚蔟索引, 不在则是非聚蔟索引

  mysql的索引与存储引擎相关, innobd  idb文件, myisan  方在 myd文件,

  innodb 是聚簇索引,myisam 中只有非聚簇索引

mysql索引结构有哪些，各自的优劣是什么 2.0.
    B+ 树

哈希索引

两种索引的使用的优势不太相同.如果是等值查询,那么哈希算法会比较快. 哈希算法若是 进行范围查询则不太行,也不支持like

### 简述mysql中索引类型有哪些，以及对数据库的性能的影响

普通索引

唯一索引

主键索引

全文索引

### Mysql的隔离级别有哪些

READ UNCOMMITED (读取未提交内容 )

READ COMMITED(读取提交内容)

REPEATEABLE READ(可重复读)

SERIALIZEABLE (可以串行化)不同的情况下出现 脏读,幻读,不可重复读

### mysql执行计划怎么看

  ```svg
  explian SQL
  ```

## SQL调优

   如何回答mysql的调优问题

   如何处理mysql的慢查询

   mysql如何进行性能监控

   schema和数据类型优化

## 锁

基础锁的属性分类: 共享锁(读锁) 排他锁(写锁)

基于锁的粒度分类: 行级别(innodb), 表级别(innodb, myisam), 页级别(innodb), 记录锁,间隙锁.临建锁.

mysql面试常见点--锁

mysql锁的类型有哪些

什么是mysql的主从复制

mysql复制的原理是什么

  通过binary log  和 IO thread 来实现
 

mysql面试常见点--索引分类

mysql面试常见点--事务
mysql面试常见点--mysql集群
 mysql面试常见点--mysql优化
 mysql面试常见点--存储引擎
 mysql面试题--mysql原子性和持久性怎么保证
 innodb和myisam区别
mysql面试题--索引分类
mysql面试题--innodb的底层数据结构

Innodb 文档 https://dev.mysql.com/doc/refman/8.0/en/innodb-storage-engine.html


mysql面试题性能监控
schema和数据类型优化
 执行计划
 索引基本常识
索引的原理
索引的优化细节
索引失效的情况

mysql主从复制原理
 mysql主从复制搭建
mysql读写分离
 事务的特点
事务的实现机制

什么是MVCC

MVCC 机制主要依赖于记录中的三个隐藏字段, undolog,read view 来实现

  DB_TRX_ID
  最近修改的事务id   
   1,2,3 代表查询 ,4 代表Update
  DB_ROLL_PTR
  7b 回滚指针
  DB_ROW_ID
  6b, 隐藏主键

MYSQL的锁机制实现
mysql为什么要存在索引系统
mysql索引应该如何设计
mysqI索引的数据结构选择
mysql索引的分类
详解mysql的回表和索引覆盖问题
详解mysql的最左匹配和索引下推
如何优雅的回答nysql索引面试题
mysql的索引原理和数据结构能介绍下吗

B+树跟B树的区别是什么
  结构不同

mysql聚簇索引和非聚簇索引的区别
  index存储的位置不同


使用mysql索引都有什么原则
如何处理mysql的慢查询

