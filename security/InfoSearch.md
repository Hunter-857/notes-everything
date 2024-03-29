# 信息收集

## DNS 信息收集

这里需要了解各种传输协议,协议的作用方便之后的信息解析

### 域名和FQDN

域名记录: A类, C类, cname, NS, MX, ptr(通过IP 反向解析域名) 

1. A Record
   
   A 类信息记录的IPV4 地址, 如:104.26.10.229

2. AAAA Record
   
   4A类信息则是记录了IPV6 地址 如:2606:4700:20::681a:be5
   
   随着移动互联网的发展联网设备越来越多, IPv4 的地址用完了,现在已经逐步转向IPV6

3. CName Record
    这些记录解析到另一个域名，例如 TryHackMe 的网店有子域名 store.tryhackme.com，它返回一个 CNAME 记录 shop.shopify.com。 然后将向 shop.shopify.com 发出另一个 DNS 请求以计算出 IP 地址。

4. MX Record
  MX记录了地址服务器
  这些记录解析为处理您正在查询的域的电子邮件的服务器的地址，例如，tryhackme.com 的 MX 记录响应看起来像 alt1.aspmx.l.google.com。 这些记录还带有优先级标志。 这告诉客户端以什么顺序尝试服务器，如果主服务器出现故障并且需要将电子邮件发送到备用服务器，这是完美的。

5. TXT Record
   
  TXT 记录是可以存储任何基于文本的数据的自由文本字段。 TXT 记录有多种用途，但一些常见的用途是列出有权代表域发送电子邮件的服务器（这有助于打击垃圾邮件和欺骗性电子邮件）。 在注册第三方服务时，它们还可用于验证域名的所有权。

6. SOA Record
   
  
7. AXFR
   
   AXFR协议(https://www.netsh.me/article/computer/dns/1151.html)

8. 连接域名解析的过程
   
   ```
       nslookup  www.baidu.com
       # 设置查询的类型
       set type 
   ```

9.  dig命令
   
   ```
   # dig 也可以反向查询 , 查询到 PTR 记录
    dig sina.com ns axfr
    or
    host -T -l sina.com ns 
   ```
   
   DNS区域传输
   
   ```
    # 对目标的DNS,服务器进行区域传输.
    dig @nsl.example.com
   ```
   
   ```shell
    # 打印了从本地到 www.baidu.com ,整个网络经过的路由情况
    traceroute  www.baidu.com 
    # 显示内容里会有一些 *** 表示设备隐藏了
   ```

### DNS字典爆破

   通过字典来 破解, 一个域名下的主机,和子域名

```shell
  # 查看 help 文档
    dnsdict -h

  #
    dnsdict  -d4 -tl 16 -x baidu.com

  #
    dnsmap 
  #
    dnsrecon
```

### DNS注册信息

  whois信息查询

```
whois baidu.com
```

 or 通过网站查询who is 信息: 
       [域名Whois查询 - 站长之家](https://whois.chinaz.com/)     [全球Whois 查询](https://www.whois365.com/cn/)

Hping3 ,Fping 命令


Meltgo 收集子域名信息

​        强大的社工工具.

暗黑版谷歌 可以搜索一下 硬件信息

​        撒旦:    https://www.shodan.io/   需要注册 ,不然会被限制  

Google hacking 语法

- intitle: 搜索网页标题中包含🈶️特定字符网页, e.g intitle:any ,这样网页标题中带有any的网页都会被搜素出来

- inurl 搜索包含特定字符的URL. e.g ‘inurl:any’

- inttext 搜索网页正文内容中的指定字符

- Filetype 搜索指定类型的文件  e.g fileType:doc . 将返回所有以doc结尾的文件

- Site: 找到指定网站有联系的URL. e.g Site: any.com

keep going on

sdfasdf


### 最新漏洞公布的网站

漏洞如何利用暂时还不会,呵呵.

- 美国著名安全公司：Exploit Database https://www.exploit-db.com/

- 赛门铁克： https://www.securityfocus.com

- 国家信息安全漏洞共享平台： https://www.cnvd.org.cn

- 国内安全厂商--绿盟科技： http://www.nsfocus.net

- 安全客： [安全客 - 安全资讯平台](https://www.anquanke.com/)

- 知道创宇漏洞库： https://www.seebug.org

- 俄罗斯知名安全实验室： https://www.securitylab.ru/vulnerability

- cve常见漏洞和披露： http://cve.mitre.org

### Nmap 端口扫描工具

功能 全链接或着 半连接扫描

Nmap 的用途: 

- 通过对设备或者防火墙的探测来测试它的安全性

- 测试主机开放的端口

- 网络存储,网络映射,维护和资产管理

- 通过识别服务器来审计网络的安全性

- 探测网络上的主机

常用的命令:

```shell
nmap -sA ip

nmap -sL ip   

nmap  -sS

nmap  -sT

nmap  -sU
```

### arp

arp-scan 回应和内置网络,向目标发送arp的package

```
# 扫描 eth0 上连接的设备
arp-scan --interface=eth0 --localnet
```

awvs

nexus

御剑

### NETCAT - NC

  又被称是: 瑞士军刀,身材小巧,功能强大。它是一个可靠的容易被其他程序所启用的后台操作工具，同时它也被用作网络的测试工具或黑客工具。 使用它你可以轻易的建立任何连接。内建有很多实用的工具。使用UDP和TCP协议。

```
# 查看帮助文档如果忘记了命令
nc -h
# 详细的命令信息
man n
```

```
 [[nc]] Telnet/Banner
 nc -nv ip port
 [[扫描]] 一定范围内的端口
 nc -nvz ip  1-2048  # tcp 协议
 nc -nvzu ip  1-2048 # upd 协议
 # exmaple
 nc -vn 192.168.1.2 80 # 80 http端口
 nc -nv 192.168.1.2 110 # 110 邮件端口
 nc -nv 192.168.1.2 20
```

```
# nc 文本传输
Server A : nc -l --4444  # 打开监听 端口
Server B : nc -nv 1.1.1.1 4444 # 另外一台电脑 连接端口

# 在A上发送, 可以传输文件, 多个文件也可以通过压缩来传递
Server A : nc -ip 333 >1.mp4   # file name
#  另外一台电脑B 上接收
Server B : nc -nv 1.1.1.1 333 < 1.mp4 -q 1 

[[甚至可以克隆]] 整个硬盘
nc -lp 333 | dd of=/dev/sda # 硬盘搞成输出流
dd if=/dev/sda | nc -nv 1.1.1.1 333 -q l # 读入标准流
```

远程连接到上代理/ 肉鸡  通过 别人对目标机 进行扫描.

## telnet 命令
telnet cs144.keithw.org http

## TCPDUMP

抓包命令

```
# -i 抓eth0  -s 指定大小  -w 指定文件
tcpdump -i eth0 -s 0  -w a.cap
```

## Dos 命令:

​ dos 命令是一般是指windows 系统下的命令

Dos 命令:

```shell
net use
net time
# 
```

### 工具 NTscan

## Regcon NG 信息收集工具
模块多样.内部集成了数据库,还可以生成框架.



### windows 中的 任务计划

远程连接 一台电脑 :

```js
 mstsc  -v   ip
```

Window 下好用 的工具 御剑

## DNS 欺骗:

攻击者冒充域名服务器

### ​ 1.ARP 欺骗 技术

```shell
# 启动服务器
systemctl start apache2
systemctl stop apache2
systemctl status apache2
```

Ettercap 工具

## 口令安全

### 弱口令

可以根据个人信息来生成一些密码

[GitHub - Mebus/cupp: Common User Passwords Profiler (CUPP)](https://github.com/Mebus/cupp)




exif 图片信息收集

hydra 工具是一种常见的暴力破解工具.它利用的是一些密码字典,社工字典,字符集字典,常用字字典.

用法: 

```shell
    hydra
```

1. ### 默认口令

2. ### 明文口令

## metasploitable安装与入侵



M0n0wall 防火墙

[m0n0wall - Downloads](https://m0n0.ch/wall/downloads.php)



Pfsense 背靠背防火墙

  https://www.pfsense.org/

网络配置使用到的命令

```
  dhclinet eht0

  ifconfig eht0 192.168.1.11/24
  route add default gw 192.168.1.1
  echo  nameserver 192.168.1.1 > /etc/resolv.conf
```

[mac 下安装adb命令_徐代龙的技术专栏-CSDN博客_mac安装adb命令](https://blog.csdn.net/xudailong_blog/article/details/109910199)

[解决adb connect 连接Android设备报错：由于目标计算机积极拒绝，无法连接 - JavaShuo](http://www.javashuo.com/article/p-aexflyur-pd.html)

就是说第一次连接电脑时候

第二次的时候就不用了

有没有什么办法让他直接连接不需要 USB确认?

./adb connect 192.168.1.4:5555

adb 命令

```
adb pull /sdcard/crime.apk 
```

- 如果想要把电脑中的文件拷贝到手机里面，使用**adb push <local> <remote>** 命令：

```
adb push crime.apk /sdcard/data/data
```

有没有什么办法让他直接连接不需要 USB确认?

./adb connect 192.168.1.4:5555

git remote add origin https://github.com/big-hunter/notes-everything.git
git push -u origin main
