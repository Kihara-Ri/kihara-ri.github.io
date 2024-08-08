# About the site

如你所见，这是一个使用[MkDocs](https://www.mkdocs.org/)搭建的Blog网站，并且使用了[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)作为主题，绝大部分的配置都可以通过查看上面的链接解决，但是我在这里想要强调的是一些需要注意的和有用的项，这些是在你面对内容庞大详实的文档时，容易变得不耐烦而忽略的点

## 配置文件

关于我的个人配置，查看: [My mkdocs.yml](https://github.com/Kihara-Ri/kihara-ri.github.io/blob/main/mkdocs.yml)

### 配置`palette`主题颜色

如果需要使用自己喜欢的颜色，在这里添加：

```yaml
- primary: custom # color of nav bar
```

然后引入`extra.css`并添加颜色配置

需要注意的是，这可能会导致亮暗模式的切换失灵，目前我还没有找到合适的解决方法

### 指定文章分类

可以在`plugins`中的`blog`中指定文章类别，防止拼写错误和随意添加，如果出了错误，在进行构建的时候引擎会报错提示

```yaml
categories_allowed:
  - Math            # 对于偏向解决单个数学问题和疑惑的，主要为分散化内容
  - CS              # 跟计算机科学相关性大的内容
  - Tutorial        # 主要为系统性教程，内容偏长
  - Language        # 学习语言时遇到的一些问题
  - Log             # 在各种折腾中对问题和过程的记录，主要为技术性实践
  - Technology      # 非常容易和前面的内容搞混淆，这里主要记录某些具体的技术
```

## 元数据 metadata

所谓的元数据，可以理解为给文章分配的属性，这是不会轻易改变的数据，也有些地方会叫做 Front-matter ，正常情况下在编辑文章的时候把元数据按下面的格式写在Markdown文件的最开头就可以，不允许开头空行且必须顶格，如果编辑器有空格的行为的话，就会导致数据失效，不起作用。在本站配置中，只需要有下面的信息就可以了：

```md
---
title:
date: 2024-01-01
categories: 
  - 在设置的预选项中选择
slug: 设置post的标题
tags: 
  - 
  - 
---
```

需要注意`categories`虽然一般情况下只有一个，但是也要求必须向上面一样以数组的形式书写

如果每次创建一个 blog 文章都要填写这样的元数据，未免有些麻烦了，因此我会使用一个 Python 脚本来完成元数据的初始化，然后我只需要将内容按照格式填写在这个文件里即可

## 摘录

如果使用`blog`插件，那么引擎就会自动抓取相应目录下的文章，并且一股脑地全部放到一个page中，这个时候就会导致信息非常多，且浏览起来不方便，引擎提供了[Adding an excerpt](https://squidfunk.github.io/mkdocs-material/setup/setting-up-a-blog/#adding-an-excerpt)功能，允许我们在Markdown中通过加入分隔符`<!-- more -->`来显示摘要，引擎会只显示标题和分隔符上面的内容，自动视其为摘要，而后面的部分则被省略

## 图标和 emojis

material 主题准备了很多可用的图标和 emoji

更多查看: [icons&emojis](https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/#with-animations-docsstylesheetsextracss)

## 更多 Markdown 扩展

如果你想使用更多的功能，查看: [Material Reference](https://squidfunk.github.io/mkdocs-material/reference/)
