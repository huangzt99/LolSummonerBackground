## 简介

修改英雄联盟生涯背景图片，可以设置未拥有的皮肤。效果如下

![](/img/demo.png)

## 使用说明

因为现在官方不再将port和token直接保存在文件里，所以需要手动获取。

在cmd中使用wmic process where caption='LeagueClientUx.exe' 可以看到port和token

![](/img/port.png)

然后将他们在程序中手动替换

![](/img/1.png)

## 实现思路

先到LOL官网爬到皮肤信息及id，在用程序模拟LOL客户端向LOL服务器发请求。

![](/img/2.png)





获取token和port方式出自B站up主[Marioㄹ]