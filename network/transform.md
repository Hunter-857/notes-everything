### 传输层

### TCP 3 次握手 建立tcp连接

192.168.1.2:8080 其中IP 指出了电脑, Port 指出那个application

路由器  上也会有一些 ip sending的 pattern ,来匹配发送的地方

you: syn ---> Sever

you: <-----syn,ack

you: --->syn,ack ,package : server

Tcp 滑动窗口原理

tcp [zero window] 数据包

tcp [keep alive] 数据包

## TCP 4次握手 , 断开的过程

tcp rst 重设标识

tcp 协议ack 协议包的偏移?

### TCP 重传技术

tcp 重新传递数据.

重传计时器.  

若干RTT value 计算 求和, 得到RTO 的value .

[ TCP Retransmission]

### UDP

### ICMP 协议

ping 就是用了 icmp 协议

### DHCP协议

应用层协议. 动态主机配置协议,是一个局域网的协议

 DHCP 服务器为客户提供IP地址 :

1.discover  -->广播

2.offer

3.request

4.ack

    
