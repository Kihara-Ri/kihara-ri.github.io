---
title: 在Markdown中插入icons
date: '2024-03-29 15:32:29'
updated: 
categories: logs
description: 
keywords: 
top_img: 
cover: https://mdstore.oss-cn-beijing.aliyuncs.com/markdown/202403292349691.png
copyright: true
mathjax: 
swiper_index: 
tags: 
  - markdown
  - html
  - css
  - hexo
  - blog
abbrlink: 在Markdown中插入icons
main_color: "#e4bf66"
---

## 写在前面

我们在浏览网站的时候，会发现别人写的Markdown文档为什么这么好看，有各种各样的效果和图案，为什么我的就没有？我连字体大小颜色都还没玩明白，别人是怎么在文章里插入这么多图标的？

经过我的一番查资料和思考，我总结了以下两个较为靠谱且满足需求的方法

当然，这里直接在markdown文档里放图片链接不算，因为既没有用到资源库自带的功能，也不如图标显示大小、风格统一和可调用性

这里我使用的是<svg class="icon" ><use xlink:href="#icon-wangluo"></use></svg><a href="https://www.iconfont.cn/">阿里巴巴矢量图形库</a>

<b><font color="#9265a6">速查：</font>
<svg class="icon" ><use xlink:href="#icon-wangluo"></use></svg>
<a href="https://www.iconfont.cn/manage/index?manage_type=myprojects&projectId=4487739">我的图标库</a></b>

引用方法：

```html
<svg class="icon" ><use xlink:href="#icon-bilibili"></use></svg>
```

## 方法1: CSS (不推荐)

使用CSS的方法引用相较来说会方便一点

<img src="https://mdstore.oss-cn-beijing.aliyuncs.com/markdown/image-20240329211822222.png" alt="image-20240329211822222" style="zoom: 33%;" />

如上图，我们进入仓库，选择`Font class`，生成代码后可以发现链接的结尾是`.css`，这就表明我们生成的链接其实是一个样式表

我们只需要在`html`标签的`<head>`标签中引入这个CSS资源

```html
<head>
<link rel="stylesheet" href="//at.alicdn.com/t/c/font_4487739_88dnmcbf2pa.css">
</head>
```

然后我们只需要用`<i>`或`<span>`标签加上类名就可以引用图标了

<link rel="stylesheet" href="//at.alicdn.com/t/c/font_4487739_88dnmcbf2pa.css">

```html
<i class="iconfont icon-bilibili"></i>
<span class="iconfont icon-youtube"></span>
```
<font color="#e3961b">这里==></font>
<center>
<i class="iconfont icon-bilibili"></i>
<span class="iconfont icon-youtube"></span>
</center>
不过...我们也能明显看出来显示的图标有什么问题🤔它们没有颜色🌈！

当然，我们可以通过以下两种方法来给图标添加颜色
- `<font color="">`(这种方法有点过时)
- `<i class="iconfont icon-<...>" style="color: <color>"></i>`(支持场景更多，但是写起来有点麻烦)

这样我们就得到了红色小电视和蓝色YouTube！
<center>
<i class="iconfont icon-bilibili" style="color:#ea3323;"></i>
<i class= "iconfont icon-youtube" style="color: #54adde"></i>
</center>

不过这种方法还是有它的优点的，根据阿里的文档`font-class`本质还是**unicode**使用方式的一种变种，也就是说它使用的还是字体，因此不支持颜色，对于不需要颜色或者颜色单一的情况下，使用CSS引入图标还是很好的，因为它的引入方式**足够简洁**

## 方法2: JS + CSS (推荐)

下面这种方法将会解决上面无法显示颜色的痛点，并且还可以调整<font color = "#8652c7">颜色</font>和<big style="font-size:24px">大</big><small style="font-size: 10px">小</small>！

首先我们再回到这个界面

<img src="https://mdstore.oss-cn-beijing.aliyuncs.com/markdown/image-20240329213405186.png" alt="image-20240329213405186" style="zoom:33%;" />

这次我们选择`Symbol`，生成代码我们发现这次的结尾是`.js`，也就是说我们这次引入的链接是正儿八经的<svg class="icon" ><use xlink:href="#icon-JavaScript"></use></svg>JavaScript编程语言了

这次我们需要用`<script>`标签来引入`js`文件，此外，我们这次引入的图标已经跟刚刚的不一样了，我们刚刚通过CSS引入的是文字，而现在我们引入的是**矢量图**`svg`文件，因此我们需要使用CSS来规定它们的大小和显示方式



```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <script src="//at.alicdn.com/t/c/font_4487739_gyxcnbnyjth.js"></script>
    <style type="text/css">
        .icon {
            width: 1em; height: 1em;
            vertical-align: -0.15em;
            fill: currentColor;
            overflow: hidden;
        }
        .icon-large {
            width: 3em; height: 3em;
            vertical-align: -0.15em;
            fill: currentColor;
            overflow: hidden;
        }
    </style>
</head>
<body>
    <svg class="icon" >
        <use xlink:href="#icon-bilibili"></use>
    </svg>
</body>
</html>
```

在这段代码中，我定义了两种图标尺寸，因为这段CSS代码是内嵌在这个markdown文档中的，而这个markdown文档经过blog框架选然后最后会成为html文件，以它该有的姿态显示在你的眼前（在我的眼里也许它就没有那么优雅了），你会注意到，表格里的图标明显比我在文档中的其他地方使用的要大，这正是两套CSS样式的好处

在声明了`<head>`之后，直接在文件里使用`<svg>`标签就可以正常使用

| Icons | Labels |
| ----- | ---- |
|  <svg class="icon-large" ><use xlink:href="#icon-youtube"></use></svg>     |  `<svg class="icon-large" ><use xlink:href="#icon-youtube"></use></svg>`    |
|  <svg class="icon-large" ><use xlink:href="#icon-JavaScript"></use></svg>     |  `<svg class="icon-large" ><use xlink:href="#icon-JavaScript"></use></svg>`      |
|   <svg class="icon-large" ><use xlink:href="#icon-lianjie"></use></svg>    |  `<svg class="icon-large" ><use xlink:href="#icon-lianjie"></use></svg>`     |
|   <svg class="icon-large" ><use xlink:href="#icon-wuxianwangluo"></use></svg>    |   `<svg class="icon-large" ><use xlink:href="#icon-wuxianwangluo"></use></svg>`   |
|   <svg class="icon-large" ><use xlink:href="#icon-meiyuan3"></use></svg>    |  `<svg class="icon-large" ><use xlink:href="#icon-meiyuan3"></use></svg>`    |
|   <svg class="icon-large" ><use xlink:href="#icon-cuowu"></use></svg>    | `<svg class="icon-large" ><use xlink:href="#icon-cuowu"></use></svg>`     |
|   <svg class="icon-large" ><use xlink:href="#icon-cuowu1"></use></svg>    |  `<svg class="icon-large" ><use xlink:href="#icon-cuowu1"></use></svg>`    |
|   <svg class="icon-large" ><use xlink:href="#icon-wangluo"></use></svg>    |  `<svg class="icon-large" ><use xlink:href="#icon-wangluo"></use></svg>`     |
|   <svg class="icon-large" ><use xlink:href="#icon-us"></use></svg>    |   `<svg class="icon-large" ><use xlink:href="#icon-us"></use></svg>`   |
|   <svg class="icon-large" ><use xlink:href="#icon-dagou"></use></svg>    | `<svg class="icon-large" ><use xlink:href="#icon-dagou"></use></svg>`      |
|   <svg class="icon-large" ><use xlink:href="#icon-cuowu2"></use></svg>    |  `<svg class="icon-large" ><use xlink:href="#icon-cuowu2"></use></svg>`    |
|   <svg class="icon-large" ><use xlink:href="#icon-zhuye"></use></svg>    |  `<svg class="icon-large" ><use xlink:href="#icon-zhuye"></use></svg>`    |
|   <svg class="icon-large" ><use xlink:href="#icon-jisuanqi"></use></svg>    |   `<svg class="icon-large" ><use xlink:href="#icon-jisuanqi"></use></svg>`    |
|   <svg class="icon-large" ><use xlink:href="#icon-heart-fill"></use></svg>    |  `<svg class="icon-large" ><use xlink:href="#icon-heart-fill"></use></svg>`    |
|   <svg class="icon-large" ><use xlink:href="#icon-riben"></use></svg>    | `<svg class="icon-large" ><use xlink:href="#icon-riben"></use></svg>`     |
|   <svg class="icon-large" ><use xlink:href="#icon-dollar"></use></svg>    |  `<svg class="icon-large" ><use xlink:href="#icon-dollar"></use></svg>`    |
|   <svg class="icon-large" ><use xlink:href="#icon-shequ"></use></svg>    |  `<svg class="icon-large" ><use xlink:href="#icon-shequ"></use></svg>`    |
|   <svg class="icon-large" ><use xlink:href="#icon-bianchengyuyan"></use></svg>   |  `<svg class="icon-large" ><use xlink:href="#icon-bianchengyuyan"></use></svg>`    |
|   <svg class="icon-large" ><use xlink:href="#icon-dagou1"></use></svg>    |   `<svg class="icon-large" ><use xlink:href="#icon-dagou1"></use></svg>`   |
|   <svg class="icon-large" ><use xlink:href="#icon-star"></use></svg>    |  `<svg class="icon-large" ><use xlink:href="#icon-star"></use></svg>`    |
|   <svg class="icon-large" ><use xlink:href="#icon-bianchengyuyan1"></use></svg>    | `<svg class="icon-large" ><use xlink:href="#icon-bianchengyuyan1"></use></svg>`     |
|   <svg class="icon-large" ><use xlink:href="#icon-china"></use></svg>    |  `<svg class="icon-large" ><use xlink:href="#icon-china"></use></svg>`   |
|   <svg class="icon-large" ><use xlink:href="#icon-info-fill"></use></svg>    |   `<svg class="icon-large" ><use xlink:href="#icon-info-fill"></use></svg>`   |
|   <svg class="icon-large" ><use xlink:href="#icon-blog"></use></svg>    |   `<svg class="icon-large" ><use xlink:href="#icon-blog"></use></svg>`   |
|   <svg class="icon-large" ><use xlink:href="#icon-ChatGPT"></use></svg>    |  `<svg class="icon-large" ><use xlink:href="#icon-ChatGPT"></use></svg>`     |
|   <svg class="icon-large" ><use xlink:href="#icon-ChatGPT-copy"></use></svg>    |  `<svg class="icon-large" ><use xlink:href="#icon-ChatGPT-copy"></use></svg>`     |
|   <svg class="icon-large" ><use xlink:href="#icon-github"></use></svg>    | `<svg class="icon-large" ><use xlink:href="#icon-github"></use></svg>`      |
|   <svg class="icon-large" ><use xlink:href="#icon-cpp"></use></svg>    | `<svg class="icon-large" ><use xlink:href="#icon-cpp"></use></svg>`     |
|   <svg class="icon-large" ><use xlink:href="#icon-rust"></use></svg>    |  `<svg class="icon-large" ><use xlink:href="#icon-rust"></use></svg>`     |
|   <svg class="icon-large" ><use xlink:href="#icon-Python"></use></svg>    |  `<svg class="icon-large" ><use xlink:href="#icon-Python"></use></svg>`     |
|   <svg class="icon-large" ><use xlink:href="#icon-bilibili"></use></svg>    |  `<svg class="icon-large" ><use xlink:href="#icon-bilibili"></use></svg>`     |
|   <svg class="icon-large" ><use xlink:href="#icon-zhihu"></use></svg>    |  `<svg class="icon-large" ><use xlink:href="#icon-zhihu"></use></svg>`    |
|   <svg class="icon-large" ><use xlink:href="#icon-curriculum"></use></svg>   |  `<svg class="icon-large" ><use xlink:href="#icon-curriculum"></use></svg>`    |
|   <svg class="icon-large" ><use xlink:href="#icon-download"></use></svg>  | `<svg class="icon-large" ><use xlink:href="#icon-download"></use></svg>` |
|   <svg class="icon-large" ><use xlink:href="#icon-weixin"></use></svg>  | `<svg class="icon-large" ><use xlink:href="#icon-weixin"></use></svg>`   |


当然，也可以采用**内联样式**
```html
<svg class="icon" style="width: 5em; height: 5em;"><use xlink:href="#icon-bilibili"></use></svg>
```

<center>
<svg class="icon" style="width: 5em; height: 5em;"><use xlink:href="#icon-bilibili"></use></svg>
</center>

## 嵌入blog框架

可以发现到这里我们在做的都是对CSS样式的修改，这个页面在html中支持得很好，正如你所看到的，但在一般的Markdown编辑器中，图标是不可显示的，在Typora中甚至不堪入目，有很多白色代码框🤣因为有大段大段的html无法正常解析内容，而且像上面那样的`html`代码在每篇文章中都需要声明一次，未免有些过于繁琐，并且维护性也不好，如果你对图标库有了新的更改，链接就可能失效，一个一个改既麻烦，又容易出错

因此如果你是在使用Hexo blog框架，使用下面的方法将图标嵌入到blog框架中

**1. 创建CSS文件**

将上面的`CSS`代码拿出来

```css
.icon {
    width: 1em; height: 1em;
    vertical-align: -0.15em;
    fill: currentColor;
    overflow: hidden;
}
.icon-large {
    width: 3em; height: 3em;
    vertical-align: -0.15em;
    fill: currentColor;
    overflow: hidden;
}
```

在blog目录下的**主题配置文件夹**中找到`source`，在`source`中会有一个`CSS`文件夹，我们创建一个新的`CSS`文件：`icon-import.css`，然后将上面的代码复制到文件里面就可以了

**2. 引入CSS文件**

在你的主题配置文件夹中找到`inject`，在这里我们可以把我们想要加入的东西插入到最后生成的`html`文件的`<head>`或`<body>`中，在这里，我们只要在`head`下加入这么一行即可：

```yml
- <link rel="stylesheet" href="/css/icon-import.css">
```

需要注意这里的语法是列表形式

**3. 引入js文件**

我们可以直接复制iconfont给我们的链接，然后按照2的方式加上

```yml
- <script src="//at.alicdn.com/t/c/font_4487739_gyxcnbnyjth.js"></script>
```

如果你考虑稳定性，并且不想每次图标库变动都重新修改，你可以将这个文件中的内容粘贴到本地，和2的做法一致

```yml
- <script src="/js/icon-import.js"></script>
```

至此，我们就可以直接通过`<svg>`标签直接引用图标了

## References

- <svg class="icon" ><use xlink:href="#icon-wangluo"></use></svg><a href="https://www.iconfont.cn/help/detail?spm=a313x.help_detail.i1.d8d11a391.4c153a81yyhgQ5&helptype=code">https://www.iconfont.cn/help/detail?spm=a313x.help_detail.i1.d8d11a391.4c153a81yyhgQ5&helptype=code</a>


如果你想添加或更改的是网站logo，请参考下面的🔗链接

- <svg class="icon" ><use xlink:href="#icon-wangluo"></use></svg><a href="https://www.w3school.com.cn/css/css_selector_attribute.asp">https://www.w3school.com.cn/css/css_selector_attribute.asp</a>



