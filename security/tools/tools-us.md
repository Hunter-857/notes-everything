Metasploit

Metasploit是一个渗透测试漏洞,是你能够查找利用和验证漏洞.


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
    
mac在打包时要给浏览器,磁盘访问权限. 这样就打包crx, perm.