## Network

以前是7 层模型,   后来被4层模型取代了

网络模型:

Application

Transport ( tcp/ip  or udp )

Network

![network4](../assets/network4.png)

Network 层

### TCP 3 次握手 建立tcp连接,

192.168.1.2:8080 其中IP 指出了电脑, Port 指出那个application

路由器  上也会有一些 ip sending的 pattern ,来匹配发送的地方

### IP The Internet Protocol (IP)

不同层级有这不同的协议.

![IP](../assets/ip.png)

Ip 层数据包的形式

IP 的格式 

IPV4  地址 0~255 ,不够用了 . 之后采用了NAT 转换技术.

最终走向IPV6

#### 子网掩码/子网划分

255.255.255.0  代表IP 的前3位都在同一个网路里.

16进制 大端与小端 ,不同的系统架构 会有不同的选择

CIDR

路由器 匹配算法 longest prefix match
路由器 会记录下 一个 forwarding table

Forwarding table is a set to CIDR

### NAT (network address translate)

NAT 服务器 [网络地址转换（NAT）的原理与配置](https://blog.51cto.com/yangshufan/1959448)

### ARP(address Resolution Protocol)

网络层协议, 可以发现 连接地址关联 网络地址 , 它直接连接了

网卡(ethernet card) 会有自己的硬件编码

工具:   [kali工具 recon-ng 的被动信息搜集_twowords的博客-CSDN博客](https://blog.csdn.net/Jaasenyi/article/details/107173402)

RTP 协议 https://blog.csdn.net/bripengandre/article/details/2238818

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
