Metasploit

Metasploit是一个渗透测试漏洞,是你能够查找利用和验证漏洞.


```shell
# 打开图形界面, 
armitage
# 若是报错找不到,则要安装
sudo apt-get update
apt-get install armitage
```

## 辅助模块
## 渗透攻击模块
## 攻击载荷模块
## 空指令模块
## 编码模块
## 后渗透模块
## Metasploit 接口

infamouse dread pirate 
fraudulent activity
mobile trail 

## ways of to be anonymous at intenet
1. acquiring the hacking machine uesed to fradulent offensive activities 也就是拿到肉鸡
2. buy a laptop which in a privacy focused crypto currency, install a liveOS which will no permanent Storage 
   also make sure full disk encryption 
   https://tails.boum.org/   保护隐私的linux 系统
   ip link -v show  # 显示硬件信息, 通过一些程序修改
   VPN 代理,等方式隐藏IP

  在这里设置一些代理 or 洋葱浏览器
   vi /etc/proxychains4.conf 
   tor start 
   proxychains firefox www.baidu.com
3. DNScat 修DNS  https://github.com/iagox86/dnscat2

## Social Engineer
一个简单的抓到别人位置的方法.
get you location by Sample Social Engineer
1. 网络抓包, 得到IP得到大概位置
2. GSP信息,通过钓鱼网站 : https://github.com/thewhiteh4t/seeker , 这样就可以知道一个人所在的经度和纬度.


clearbot https://phonebook.cz

emailhippo


[神奇的网站](https://jubt.live/cn/index.html)

web3 解释 https://www.youtube.com/watch?v=nHhAEkG1y2U


彩虹屁语音: https://github.com/SaekiRaku/vscode-rainbow-fart

vs 插件开发介绍:  https://blog.csdn.net/weixin_33809981/article/details/93922280
freelance指导:   https://www.youtube.com/watch?v=4TIvB8zDFio

======================
infamouse dread pirate 
fraudulent activity
mobile trail 

1. acquiring the hacking machine uesed to fradulent offensive activities  也就是拿到肉鸡
2. buy a laptop which in a privacy focused crypto currency, install a liveOS which will no permanent Storage 
   also make sure full disk encryption 
   https://tails.boum.org/   保护隐私的linux 系统
   ip link -v show  # 显示硬件信息, 通过一些程序修改
   VPN 代理,等方式隐藏IP
   # 在这里设置一些 代理
   vi /etc/proxychains4.conf 
   tor start 
   proxychains firefox www.baidu.com
3. DNScat 修DNS  https://github.com/iagox86/dnscat2

<img width="1124" alt="screen shot" src="https://user-images.githubusercontent.com/12094603/154958717-4877e1b7-ffa3-4117-9464-f77ad317bff4.png">




[Chorme 应用](https://developer.chrome.com/docs/apps/)

插件教程:
    https://www.ituring.com.cn/book/miniarticle/60224?bookID=1421&type=minibook&subject=%E7%AC%AC2%E7%AB%A0%E3%80%80Chrome%E6%89%A9%E5%B1%95%E5%9F%BA%E7%A1%80
[Chorme 插件](https://developer.chrome.com/docs/extensions/)
what ii extensions

官方提供的sample https://github.com/GoogleChrome/chrome-extensions-samples ,可以参考.
就是这么一个 manifest.json + (h5+css+js) + images 工程.
组成:
    1. manifest.json 文件
    2. HTML文件、CSS样式文件、JavaScript、图片等静态文件
   
浏览器 会按照manifest.json内容是按照一定格式描述的扩展相关信息，如扩展名称、版本、更新地址、请求的权限、扩展的UI界面入口等等

官方给出的mainfest,version mv3: 详细信息:https://developer.chrome.com/docs/extensions/mv3/intro/

总的chorme API : https://developer.chrome.com/docs/extensions/reference

所有属性的在这里查看 https://developer.chrome.com/docs/extensions/reference/extension/

manifest 里的一些基本属性:

    允许跨域,可以用来配置自己的API地址.

        ```
            {
                ...
                "permissions": [
                    "{config url}"
                ]
            }
        ```
    
tips: mac在打包时要给浏览器,磁盘访问权限. 这样就打包crx, perm.


1. 前端通过JS监听了,记录人物移动步数. 之后会通过Ajax 调用后端接口存储数据
2. Bootstrap 提供的珊格化布局,https://v3.bootcss.com/css/#grid
     example:  <div class="container-fluid">
                <div class="row">
                    ...
                </div>
            </div>

3. 游戏实现方式:js渲染div,
     3.1:  先画地图 --> 人物 --> 箱子
          game.html/ mapdata: [] 控制地图数据
          0-绿色北京, 1-墙, 2-位置球 3-盒子, 4-人物
     3.2: 控制人物移动
          game.html/ controlPerson : function(){......
                     controlFn: function 
     3.3: 判断人物和障碍物位
          game.html/   collision: function 
4. 遇到问题
    
  查看手册: 
     jquery:https://www.jquery123.com/
     flask: http://www.pythondoc.com/flask/quickstart.html
     flaskSQL: http://www.pythondoc.com/flask-sqlalchemy/api.html#flask.ext.sqlalchemy.SQLAlchemy
     bootstrapt: https://v3.bootcss.com/
  社区提问:https://stackoverflow.com/
  
  google or 百度

5.  html是一种文本标记语言,通过标签来指出页面上的内容, css 则是一种样式表,负责指出页面上div的样式 如: margin ,padding ,display 

    Document Object Model 是html的树型结构 
    HTML DOM 定义了访问和操作 HTML 文档的标准方法。 
    DOM 以树结构表达 HTML 文档。 https://www.runoob.com/htmldom/htmldom-tutorial.html
    
     The differences between World Wide Web and the Internet
     1. WWW consists of content organized as web pages. The Web pages are available across the Internet from web servers; HTTP/HTTPS protocol is use to transfer the web pages from server to client;
     
     2. The Internet is a connected network, a global communication infrastructure. It links computers and networks together. The Internet uses TCP/IP suite to provide various services, including the web service, email service, file transfer service and many others.

    用div标记了页面结构 ,借助bootstrap的全局样式, class: contains > row > col-md-6
        <div class="row show-grid">
            <div id="personalInfo" class="thumbnail col-md-6 col-md-offset-3">
                <div class="caption"></div>
            </div>
        </div>

    JS 可以有面向对象的思想来编辑, 如这个项目中 game.html 中 js 就是采用了面向对象的方式来编辑game.js
    game 对象中有 init, createMap ,controlPerson 代表对象的能力
    size(地图方格子数),level(初始化登记),stepNum(步数),mapDate(地图数据)都是对象的属性,

     
    function replace() {
       var userInput =  $("#userInput").val()
       return userInput == "test" ? userInput.replace("test","XXXX"): userInput; 
    }