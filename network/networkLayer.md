## Network

以前是7 层模型,   后来被4层模型取代了

网络模型:

Application

Transport ( tcp/ip or udp )

Network 层

连接层

7层协议模型与4层的对照关系

![network7](../assets/network7to4.png)

![network4](../assets/network4.png)

### IP The Internet Protocol (IP)

不同层级有这不同的协议.

![IP](../assets/ip.png)

Ip 层数据包的形式

IP 地址的编址方式经历了三个历史阶段：

- 分类
- 子网划分
- 无分类

#### 分类

由两部分组成，网络号和主机号，其中不同分类具有不同的网络号长度，并且是固定的。

IP 地址 ::= {< 网络号 >, < 主机号 >}
IP 的格式

| A类地址 A | 0.0.0.0 |  125.0.0.1 |
| --------- | ------- | -------- |
| A类地址   | 0.0.0.0 |           |
| B类地址   | 0.0.0.0 |          |
| C类地址   | 0.0.0.0 |          |
| D类地址   |         |          |


IPV4  地址 0~255 ,不够用了 . 之后采用了NAT 转换技术.

最终走向IPV6
网络地址 和 设备地址
#### 子网掩码/子网划分
根据子网掩码, 确定那个是网络地址 ,那个是设备地址.
255.255.255.0  代表IP 的前3位都在同一个网路里.

16进制 大端与小端 ,不同的系统架构 会有不同的选择

#### 无分类 CIDR

路由器 匹配算法 longest prefix match
路由器 会记录下 一个 forwarding table

Forwarding table is a set to CIDR

可以通过 TTL 的值来判断, 2个设备之前有多少设备.

IP 分片  <https://www.bilibili.com/video/BV1B5411h7t4?p=7&spm_id_from=pageDriver>

### ARP(address Resolution Protocol)

网络层协议, 可以发现 连接地址关联 网络地址 , 它直接连接了
网卡地址(ethernet card address)  48 bit的16进制数字 e.g 9.9.9.9
硬件mac码


### NAT (network address translate)

NAT 服务器 [网络地址转换（NAT）的原理与配置](https://blog.51cto.com/yangshufan/1959448)



工具:   [kali工具 recon-ng 的被动信息搜集_twowords的博客-CSDN博客](https://blog.csdn.net/Jaasenyi/article/details/107173402)

RTP 协议 <https://blog.csdn.net/bripengandre/article/details/2238818>



### 无线网络
802.11 标准















hypothetical   假想的
hypothetically 假想滴
decoupled with  解偶
wild cards  通配符

partial           部分的

rendezvous  会合

relay

hop                      跳
corruption      腐败

thin waist

voltage

analogy mode   类比模式

postal service

a bare bone service
assumption
concludes
stuck in a loop
brown goes to ocean
controverial and revolutionary idea

assembly code
encapsulate

representation big endian or little endian


```
export ANT_HOME=/Users/hunter/Documents/drawIO/ant
export PATH=${PATH}:${ANT_HOME}/bin
```

```
docker build -t draw_io:v1.0 -f ./Dockerfile 
```
