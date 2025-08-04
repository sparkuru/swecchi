<p align = "center" style="font-size: 34px;" > <strong>「SHANWER ECCHI !」</strong> </p>

Shanwer：我喜欢你，REACT + GIN + GORM

## 使用方法！

通过向 url 传递不同的参数来自定义徽章，首先魔法起手式：`https://domain.com/api/swecchi?args`，后面接的 args 参数可以如下（使用 `&` 符来连接多个参数）！

- `url`：`url=https://avatars.githubusercontent.com/u/16631550`，换显示的图标！**这里放一个换了图标的徽章**
- `backcolor`：`backcolor=0000ff`，来设定背景颜色，默认的背景颜色会随图片改变，是自动生成的！**这里放一个换了背景颜色的徽章**
- `fontcolor`：`fontcolor=0000ff`，来设定文字的颜色，默认的文字颜色取决于背景颜色，通常使用白字，背景颜色的亮度高时使用黑字！**这里放一个换了字体颜色的徽章**
- `scale`：`scale=2`，来让你的徽章整个等比例放大！**这里放一个放大了的徽章**
- `text`：`text=草`，来显示徽章的文本！**这里放一个显示文本的徽章**
- `border`：`border=4`，来设置徽章的边距和阴影扩散范围！**太麻烦了我不想写了**
- `barlen`：`barlen=10`，来设定徽章的文字条的长度，默认的长度是由文本决定的！
- `size`：`size=50`，设定徽章尺寸，但是字号不会变！
- `fontsize`：`frontsize=30`，可以设定字体大小了！
- `barradius`：`barradius=999`，设定文本条的援交！
- `anime`：`anime=5`，还可以设定文本条弹出的动画时间！
- `shadow`：`shadow=0.9`，设定背景阴影的浓度！
- `repo`：`repo=account_name/repo_name`，**特殊参数**，可以主动获得对应 repo 的名字和斯达数！

## 头脑风暴！

-   自动 sw 翻译机！将你说的话 sw 化！[RimoChan/yinglish](https://github.com/RimoChan/yinglish.git)
-   e77h1！意大利面拌 42 号混凝土！[RimoChan/i7h](https://github.com/RimoChan/i7h.git)，[RimoChan/bnhhsh](https://github.com/RimoChan/bnhhsh.git)
-   不用存储的图床！你可以上传一张图片，我用文本给你存，到时候你只要用数据来还原就行了！[RimoChan/emmmbedding](https://github.com/RimoChan/emmmbedding.git)
-   ~~fi~~swecchi 搜索引擎！你可以通过 api 和这个搜索引擎交互，给你返回更~~没~~有用的信息！[RimoChan/sese-engine](https://github.com/RimoChan/sese-engine.git)，[莉沫酱的数据集！](https://github.com/RimoChan/internet-dataset.git)
-   超！使用魔法加速引擎使我的 python 代码更快更强！[RimoChan/chao](https://github.com/RimoChan/chao.git)
-   反和谐超级武器！元必有象，象必唯一！[RimoChan/unvcode](https://github.com/RimoChan/unvcode.git)

## 架构！

![](https://raw.githubusercontent.com/RimoChan/unv-shield/slave/文档/q.png)

- 服务的核心是Azure上的一个Function App<sub>(FAAS)</sub>。
- 用cloudflare做了一层HTTP缓存，可以省钱。
- 通过GitHub访问时还会过一层Camo缓存。
- 活死人的呼声是一个定时触发器，用来防止unv-shield冷启动。

## ❤赞助❤

如果你觉得 swecchi 对你的工作或学习有所帮助，欢迎往原作者：[RimoChan](https://github.com/RimoChan) 的邮箱 [the@librian.net](mailto:the@librian.net) 里发萝莉图片以表达谢意！