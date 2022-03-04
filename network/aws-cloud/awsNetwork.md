# Aws Global Infrostruct
## Region

### AWS VPC
https://www.youtube.com/watch?v=g2JOHLHh4rI
最主要的还是可以看[官网](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)的文档介绍

在使用VPC 之前,我们需要了解一些基本的网络协议 [IPV4](../network/networkLayer.md) ,不能对地址路由这些东西,一脸懵逼.



### 概念
VPC: 是你在AWS的虚拟网络,就像是在aws的虚拟数据中心,它可以分配和隔绝不同云主机. 为你提供整个网络控制权限,包括了IP ,子网划分,route table 和 gateways 配置,之后你就在可以在你的VPC中启动 EC2 实例,云函数,Dynamic DB 等.

VPC的核心内容:
Region: 是指在页面上选择的地区,香港,华南,华北,纽约什么的都有,我们在一个 Region下可以配置VPC.
一个Region下可以有多个VPC,也可以只有一个.(这完全和钱有关...)
在VPC中可以设置私有subnet 或者公共有subnet.
公网和私网之前要通过路由来通信,需要配置Route map.只有公共subnet 才有公网IP ,才能访问外网.
也可以是多个 vpc
![VPC](../assets/vpc.png) 

### CIDR and subnet:
当你创建一个VPC时,你必须声明IP和子网

When you create a VPC, you must specify a range of IPV4 addresses for the VPC in the form of a Classless Inter-Domain
Routing (CIDR) block; for example, 10.0.0.0/16

• A VPC spans all the Availability Zones in the region
• You have full control over who has access to the AWS resources
inside your VPC
AWS中一个Regiin 下默认可以创建5个VPC
• A default VPC is created in each region with a subnet in each AZ

### 推荐设置
• CIDR 的大小最好在 /16 和 /28 之间,修改这个会话费很长时间
• The CIDR block must not overlap with any existing CID block
that's associated with the VPC
• You cannot increase or decrease the size of an existing CIDR
block
• The first four and last IP address are not available for use
• AWS recommend you use CID blocks from the FC 1918
ranges:
| RFC 1918 Range                                  | Example CIDR Block                                          | 
| ----------------------------------------------- | ----------------------------------------------------------- | 
| 10.0.0.0 - 10.255.255.255 (10/8 prefix)         | Your VPC must be /16 or smaller, for example, 10.0.0.0/16   | 
| 172.16.0.0 - 172.31.255.255 (172.16/12 prefix)  | Your VPC must be /16 or smaller, for example, 172.31.0.0/16 | 
| 192.168.0.0-192.168.255.255 (192.168/16 prefix) | Your VPC can be smaller, for example 192.168.0.0/20(4)      | 

Ensure you have enough networks and hosts
Bigger CIDR blocks are typically better(more flexibility)
Smaller subnets are OK for most use cases
Consider deploying application tiers per subnet
Split your HA resources across subnets in different AZS
VPC Peering requires non-overlapping CIDR blocks
This is across all VPCS in all Regions/accounts you want to connect
Avoid overlapping (IDR blo as much as possible!

### Credit VPC
点点点, 按照提示点就可以了,当然也可以尝试使用terrorform.

可以通过 AWC CLI ec2 发布到指定网络.
```
aws ec2 run-instances --image-id<> -instance-type<>  --security-group-ids<au> --subnet-id<> -key-name<>  --user-data<>
```

### Security Group and Network ACL

Network ACL (Network Access Control) 在 子网中过滤流量 ,答到访问控制的效果.
需要控制 inbound/outbound 的规则.
Security Group 则是在ec2之前控制访问权限. 就是一些端口配置感觉各种云服务都差不多.

一个典型的VPC设置:
![vpc class](../assets/aws_vpc.png)


### VPC Peering

连接IPV4 ,IPV6 在不同协议下的VPCs.
可以是同一个 region 下的,
vpc endpionts

aws client vpn
- Create VPC EndPoint: https://www.youtube.com/watch?v=g2JOHLHh4rI&t=1h26m41s
- AWS Client VPN: https://www.youtube.com/watch?v=g2JOHLHh4rI&t=1h36m55s
- AWS Site-to-Site VPN: https://www.youtube.com/watch?v=g2JOHLHh4rI&t=1h39m43s
- AWS VPN CloudHub: https://www.youtube.com/watch?v=g2JOHLHh4rI&t=1h41m51s
- AWS Direct Connect (DX): https://www.youtube.com/watch?v=g2JOHLHh4rI&t=1h44m50s
- AWS Direct Connect Gateway: https://www.youtube.com/watch?v=g2JOHLHh4rI&t=1h51m31s
- AWS Transit Gateway: https://www.youtube.com/watch?v=g2JOHLHh4rI&t=1h54m59s
- Using IPv6 in a VPC: https://www.youtube.com/watch?v=g2JOHLHh4rI&t=1h58m54s
- Create VPC Flow Logs: https://www.youtube.com/watch?v=g2JOHLHh4rI&t=2h04m55s


可以配置路由