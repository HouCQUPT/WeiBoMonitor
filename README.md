WeiBoMonitor
微博更新邮件通知
==============
0x00 思路
==========
微博API：“www.weibo.cn/usr”
使用 Requsts 抓取目标微博的信息，使用BesutifulSoup解析HTML信息，分析对比标签ID，判断是否目标用户是否更新微博<bar>

0X01 配置信息
=============

目标用户URL配置
-------------------
通过"www.weibo.cn" 登录微博，得到目标微博的URL，格式为：”weibo.cn/u/<user ID>“,将URL复制到WeiBoMonitor.py的__main__中

邮箱配置config.txt
-------------------
发送邮箱使用QQ邮箱，需要开启QQ邮箱SMTP服务以获取授权码，获得授权码后将授权码copy到config.txt文件的license字段
收信邮箱没有限制，选取自己任意可以随时看到的邮箱地址

微博Cookies配置
-------------------
登录 “www.weibo.cn” 微博后，获取cookie，复制cookie到cookie.txt文件

0x02 运行
=============
clone到本地后，使用编辑器打开.py 文件，正确配置相关信息即可运行，每五分钟扫描一次目标微博，若更新则发送邮件提示
