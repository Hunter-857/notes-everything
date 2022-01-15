# 信息收集

## Kail 命令

kail 是linux 的一个版本所以熟悉linux 命令也会熟悉Linux命令.

查看DNS 信息

1. nslookup  

2. dig 

3. whois  命令 or 网站
   
   ```shell
   whois xuegod.cn
   ```
   
   cdn
   
   ```shell
   traceroute  www.baidu.com 
   # 打印了从本地到 www.baidu.com ,整个网络经过的路由情况
   # 显示内容里会有一些 *** 表示设备隐藏了
   ```
   
   Hping3 ,Fping 命令

Meltgo 收集子域名信息

​        强大的社工工具.

暗黑版谷歌 可以搜索一下 硬件信息

​        撒旦:    https://www.shodan.io/   需要注册 ,不然会被限制  

Google hacking 语法

- intitle: 搜索网页标题中包含🈶️特定字符网页, e.g intitle:any ,这样网页标题中带有any的网页都会被搜素出来

- inurl 搜索包含特定字符的URL. e.g ‘inurl:any’

- inttext 搜索网页正文内容中的指定字符

- Filetype 搜索指定类型的文件  e.g fileType:doc . 将返回所有以doc结尾的文件

- Site: 找到指定网站有联系的URL. e.g Site: any.com

### 最新漏洞公布的网站

漏洞如何利用暂时还不会,呵呵.

- 美国著名安全公司：Exploit Database   https://www.exploit-db.com/

- 赛门铁克：  https://www.securityfocus.com

- 国家信息安全漏洞共享平台： https://www.cnvd.org.cn

- 国内安全厂商--绿盟科技： http://www.nsfocus.net

- 安全客： https://www.anquanke.com/

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
nmap 
```

### NC 扫描端口

    又被称是: 瑞士军刀

    用途:

   用法:

远程连接到上代理/ 肉鸡  通过 别人对目标机 进行扫描.

## Dos 命令:

​ dos 命令是一般是指windows 系统下的命令

 Dos 命令:

```shell
net use
net time
# 
```

### 工具 NTscan

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

​  hydra 工具是一种常见的暴力破解工具.它利用的是一些密码字典,社工字典,字符集字典,常用字字典.

用法: 

```shell
hydra
```

1. ### 默认口令

2. ### 明文口令

![](/Users/hunter/Desktop/book/notes_everything/assets/qrcode.jpg)
