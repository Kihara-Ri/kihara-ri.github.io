# 关于个人主页的构建

这个仓库用来存放静态网站的数据，网站使用 Mkdocs 搭配 GitHub Pages 构建

目前仍存在的问题: 

1. 有一些 Markdown 语法没有很好地支持，如`**`加粗文本等
2. 代码框没有`复制`按键
3. `mermaid`渲染暂不支持
4. `blog`拦会显示所有的posts文章，如果不添加`<!-- more -->`就会显示全文，不利于检索，访问速度也会变慢
5. 锚点存在问题，如果文章名没有英文，锚点链接就不会正常生成，全都会被简化成数字，这时候点击锚点的时候就会出现冲突；而有些文章名存在英文，一旦英文名存在冲突，点击锚点就会跳转到第一个，后面的文章可以说不存在正确跳转的锚点了