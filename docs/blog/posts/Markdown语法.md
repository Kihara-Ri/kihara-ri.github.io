---
layout: pages
title: Markdown语法
date: 2023-12-26
tags: 
  - Markdown
categories: 
  - Technology
---

# Markdown语法

[Markdown官方教程](https://www.markdownguide.org/getting-started/)

Markdown的语法非常丰富，虽然表面上Markdown能做的事很少，但是只要嵌入html就一切皆有可能，在这里我列下可以参考的文档以供快速查找：

1. 使用数学公式参见`LaTe常用表达式`
2. 使用`Mermaid`画图参见`Mermaid语法`


## 快捷键

使用typora的时候，进入源代码模式可以使用`⌘command+/`

## 嵌入视频

- https://support.typora.io/Media/
- https://gist.github.com/tzmartin/1cf85dc3d975f94cfddc04bc0dd399be

bilibili视频可以按下面的方法嵌入：

```html
<iframe width="560" height="315" src="//player.bilibili.com/player.html?aid=459231629&bvid=BV1E5411E71z&cid=297079639&p=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>
```

YouTube视频可以按下面的方法嵌入：

```html
<iframe width="560" height="315" src="https://www.youtube.com/embed/Wz50FvGG6xU" frameborder="0"  allowfullscreen></iframe>
```

事实上在b站和YouTube上都可以在分享中找到嵌入的方式，YouTube的嵌入可以直接使用，b站的嵌入需要稍微调整一下参数，建议直接复制上面的嵌入方法

## 并排插入图片

通过`figure`标签可以实现在Markdown中并排插入图片：

```html
<center>
<figure class = "half">
    <img src = "https://mdstore.oss-cn-beijing.aliyuncs.com/Screenshot%202023-10-18%20at%2015.52.59.png" width = "350">
    <img src = "https://mdstore.oss-cn-beijing.aliyuncs.com/Screenshot%202023-10-18%20at%2015.53.13.png" width = "350">
</figure>
</center>
```

<center>
<figure class = "half">
    <img src = "https://mdstore.oss-cn-beijing.aliyuncs.com/Screenshot%202023-10-18%20at%2015.52.59.png" width = "350">
    <img src = "https://mdstore.oss-cn-beijing.aliyuncs.com/Screenshot%202023-10-18%20at%2015.53.13.png" width = "350">
</figure>
</center>


但是这种方法无法在hexo上正常使用，所以如果需要发布的话，优先考虑使用表格的方法：

<center>
<table><tr>
  <td><img src="https://mdstore.oss-cn-beijing.aliyuncs.com/Screenshot%202023-10-18%20at%2015.52.59.png" width = "350"></td>
  <td><img src="https://mdstore.oss-cn-beijing.aliyuncs.com/Screenshot%202023-10-18%20at%2015.53.13.png" width = "350"></td>
</tr></table>
</center>


## 注音


```html
<ruby>ご<rt></rt>飯<rp>（</rp><rt>はん</rt><rp>）</rp></ruby>
```

<ruby>ご<rt></rt>飯<rp>（</rp><rt>はん</rt><rp>）</rp></ruby>



## 嵌入html

嵌入如下代码来构造一个按钮控件：

```html
<!-- 在Hexo博客文章中嵌入的HTML按钮 -->
<center>
<button id="abutton" onclick="displayAlert()" >点击我</button>
</center>

<style>
    #abutton {
        background-color: #4CAF50; /* 绿色背景 */
        color: white; /* 白色文字 */
        padding: 15px 32px; /* 上下15px，左右32px的内边距 */
        text-align: center; /* 文字居中 */
        text-decoration: none; /* 无文本装饰 */
        display: inline-block; /* 行内块级元素 */
        font-size: 16px; /* 字体大小 */
        margin: 4px 2px; /* 外边距 */
        cursor: pointer; /* 鼠标指针变为手指形状 */
        border: none; /* 无边框 */
        border-radius: 5px; /* 圆角半径5px */
        transition-duration: 0.4s; /* 过渡动画持续时间 */
    }

    #abutton:hover {
        background-color: #45a049; /* 鼠标悬停时的背景颜色 */
    }
</style>

<script>
function displayAlert() {
    alert("你点击了按钮！");
}
</script>

```

{% raw %}

<!-- 在Hexo博客文章中嵌入的HTML按钮 -->

<center>
<button id="abutton" onclick="displayAlert()" >点击我</button>
</center>

<style>
    #abutton {
        background-color: #4CAF50; /* 绿色背景 */
        color: white; /* 白色文字 */
        padding: 15px 32px; /* 上下15px，左右32px的内边距 */
        text-align: center; /* 文字居中 */
        text-decoration: none; /* 无文本装饰 */
        display: inline-block; /* 行内块级元素 */
        font-size: 20px; /* 字体大小 */
        margin: 4px 2px; /* 外边距 */
        cursor: pointer; /* 鼠标指针变为手指形状 */
        border: none; /* 无边框 */
        border-radius: 5px; /* 圆角半径5px */
        transition-duration: 0.4s; /* 过渡动画持续时间 */
    }

    #abutton:hover {
        background-color: #209e20; /* 鼠标悬停时的背景颜色 */
    }
</style>

<script>
function displayAlert() {
    alert("你点击了按钮！");
}
</script>

{% endraw %}


## JavaScript动画


{% raw %}
<!DOCTYPE html>
<html>
<head>
    <title>单位向量旋转示例</title>
    <style>
        #canvas-container {
            text-align: center;
        }
        canvas {
            border: 4px solid black;
            margin: auto;
            display: block;
        }
    </style>
</head>
<body>
    <div style="text-align: right;">
    <button id="toggleAnimation" >toggle</button>
    </div>
    <style>
        button {
        padding: 10px 20px; /* 内边距 */
        font-size: 16px; /* 字体大小 */
        color: white; /* 字体颜色 */
        background-color: #007BFF; /* 背景色 */
        border: none; /* 无边框 */
        border-radius: 5px; /* 圆角边框 */
        cursor: pointer; /* 鼠标悬停时的光标形状 */
        outline: none; /* 点击时不显示轮廓 */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 盒子阴影 */
        transition: all 0.2s ease; /* 过渡效果 */
    }

        button:hover {
            background-color: #0056b3; /* 悬停时的背景色 */
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2); /* 悬停时的阴影 */
        }
    
        button:active {
            background-color: #004085; /* 点击时的背景色 */
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* 点击时的阴影 */
        }
    </style>

<div class="flex-container">
    <div id="canvas-container">
        <canvas id="canvas" width="400" height="400" class="div-item"></canvas>
    </div>
    <div id="matrixValue"></div>
</div>
<style>
    .flex-container {
        display: flex;
    }
    .div-item{
        margin-right: 80px; /* 右外边距 */
    }
</style>

    <!-- 引入MathJax库 -->
    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    
    <script>
        var isAnimating = false; // 动画状态标志
        var animationFrameId;
    
        document.getElementById('toggleAnimation').addEventListener('click', function() {
            if (isAnimating) {
                cancelAnimationFrame(animationFrameId); // 停止动画
                this.textContent = 'toggle';
                isAnimating = false;
            } else {
                isAnimating = true;
                this.textContent = 'pause';
                update(); // 开始动画
            }
        });
        var canvas = document.getElementById('canvas');
        var ctx = canvas.getContext('2d');
        var matrixValueDiv = document.getElementById('matrixValue');
    
        var angle = 0; // 初始角度
        var angleIncrement = Math.PI / 480; // 每次旋转的角度增量
    
        function drawCoordinateSystem() {
            ctx.beginPath();
            ctx.moveTo(200, 0);
            ctx.lineTo(200, 400);
            ctx.moveTo(0, 200);
            ctx.lineTo(400, 200);
            ctx.strokeStyle = 'rgba(0, 0, 0, 0.2)';
            ctx.stroke();
        }
    
        function drawVector() {
            var x = 100 * Math.cos(angle);
            var y = 100 * Math.sin(angle);
            ctx.beginPath();
            ctx.moveTo(200, 200);
            ctx.lineTo(200 + x, 200 - y);
            ctx.strokeStyle = '#faad14';
            ctx.lineWidth = 3;
            ctx.stroke();
            
            // 绘制箭头
            var arrowSize = 10; // 箭头的大小
            ctx.beginPath();
            ctx.moveTo(200 + x, 200 - y);
            ctx.lineTo(200 + x - arrowSize * Math.cos(angle - Math.PI / 6), 200 - y + arrowSize * Math.sin(angle - Math.PI / 6));
            ctx.lineTo(200 + x - arrowSize * Math.cos(angle + Math.PI / 6), 200 - y + arrowSize * Math.sin(angle + Math.PI / 6));
            ctx.lineTo(200 + x, 200 - y);
            ctx.fillStyle = 'red';
            ctx.fill();
        }
    
        function drawVectorTipCircle() {
            ctx.beginPath();
            ctx.arc(200, 200, 100, 0, 2 * Math.PI);
            ctx.strokeStyle = '#03befc';
            ctx.lineWidth = 3;
            ctx.stroke();
        }
    
        function updateMatrixValue() {
            var angleDegrees = Math.round(angle * (180 / Math.PI)); // 将弧度转换为角度
            matrixValueDiv.innerHTML = `旋转矩阵：<br>\\[\\begin{bmatrix} \\cos(${angleDegrees}^\\circ) & -\\sin(${angleDegrees}^\\circ) \\\\ \\sin(${angleDegrees}^\\circ) & \\cos(${angleDegrees}^\\circ) \\end{bmatrix}\\]`;
    
            MathJax.typeset(); // 更新MathJax渲染
}


        function update() {
            
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            drawCoordinateSystem();
            drawVectorTipCircle();
            drawVector();
            updateMatrixValue();
    
            if (!isAnimating) return; // 如果动画被暂停，则不执行后续操作
    
            angle += angleIncrement; // 更新角度
            angle = angle % (2 * Math.PI); // 当角度达到2π时重置为0
            requestAnimationFrame(update); // 请求下一帧
        }
    
        update();
    </script>
</body>
</html>

{% endraw %}

以下为显示动画的源代码：

```html
{% raw %}
<!DOCTYPE html>
<html>
<head>
    <title>单位向量旋转示例</title>
    <style>
        #canvas-container {
            text-align: center;
        }
        canvas {
            border: 4px solid black;
            margin: auto;
            display: block;
        }
    </style>
</head>
<body>
    <div style="text-align: right;">
    <button id="toggleAnimation" >toggle</button>
    </div>
    <style>
        button {
        padding: 10px 20px; /* 内边距 */
        font-size: 16px; /* 字体大小 */
        color: white; /* 字体颜色 */
        background-color: #007BFF; /* 背景色 */
        border: none; /* 无边框 */
        border-radius: 5px; /* 圆角边框 */
        cursor: pointer; /* 鼠标悬停时的光标形状 */
        outline: none; /* 点击时不显示轮廓 */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 盒子阴影 */
        transition: all 0.2s ease; /* 过渡效果 */
    }

        button:hover {
            background-color: #0056b3; /* 悬停时的背景色 */
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2); /* 悬停时的阴影 */
        }

        button:active {
            background-color: #004085; /* 点击时的背景色 */
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* 点击时的阴影 */
        }
    </style>

<div class="flex-container">
    <div id="canvas-container">
        <canvas id="canvas" width="400" height="400" class="div-item"></canvas>
    </div>
    <div id="matrixValue"></div>
</div>
<style>
    .flex-container {
        display: flex;
    }
    .div-item{
        margin-right: 80px; /* 右外边距 */
    }
</style>

    <!-- 引入MathJax库 -->
    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

    <script>
        var isAnimating = false; // 动画状态标志
        var animationFrameId;

        document.getElementById('toggleAnimation').addEventListener('click', function() {
            if (isAnimating) {
                cancelAnimationFrame(animationFrameId); // 停止动画
                this.textContent = 'toggle';
                isAnimating = false;
            } else {
                isAnimating = true;
                this.textContent = 'pause';
                update(); // 开始动画
            }
        });
        var canvas = document.getElementById('canvas');
        var ctx = canvas.getContext('2d');
        var matrixValueDiv = document.getElementById('matrixValue');

        var angle = 0; // 初始角度
        var angleIncrement = Math.PI / 480; // 每次旋转的角度增量

        function drawCoordinateSystem() {
            ctx.beginPath();
            ctx.moveTo(200, 0);
            ctx.lineTo(200, 400);
            ctx.moveTo(0, 200);
            ctx.lineTo(400, 200);
            ctx.strokeStyle = 'rgba(0, 0, 0, 0.2)';
            ctx.stroke();
        }

        function drawVector() {
            var x = 100 * Math.cos(angle);
            var y = 100 * Math.sin(angle);
            ctx.beginPath();
            ctx.moveTo(200, 200);
            ctx.lineTo(200 + x, 200 - y);
            ctx.strokeStyle = '#faad14';
            ctx.lineWidth = 3;
            ctx.stroke();
            
            // 绘制箭头
            var arrowSize = 10; // 箭头的大小
            ctx.beginPath();
            ctx.moveTo(200 + x, 200 - y);
            ctx.lineTo(200 + x - arrowSize * Math.cos(angle - Math.PI / 6), 200 - y + arrowSize * Math.sin(angle - Math.PI / 6));
            ctx.lineTo(200 + x - arrowSize * Math.cos(angle + Math.PI / 6), 200 - y + arrowSize * Math.sin(angle + Math.PI / 6));
            ctx.lineTo(200 + x, 200 - y);
            ctx.fillStyle = 'red';
            ctx.fill();
        }

        function drawVectorTipCircle() {
            ctx.beginPath();
            ctx.arc(200, 200, 100, 0, 2 * Math.PI);
            ctx.strokeStyle = '#03befc';
            ctx.lineWidth = 3;
            ctx.stroke();
        }

        function updateMatrixValue() {
            var angleDegrees = Math.round(angle * (180 / Math.PI)); // 将弧度转换为角度
            matrixValueDiv.innerHTML = `旋转矩阵：<br>\\[\\begin{bmatrix} \\cos(${angleDegrees}^\\circ) & -\\sin(${angleDegrees}^\\circ) \\\\ \\sin(${angleDegrees}^\\circ) & \\cos(${angleDegrees}^\\circ) \\end{bmatrix}\\]`;

            MathJax.typeset(); // 更新MathJax渲染
}


        function update() {
            
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            drawCoordinateSystem();
            drawVectorTipCircle();
            drawVector();
            updateMatrixValue();

            if (!isAnimating) return; // 如果动画被暂停，则不执行后续操作

            angle += angleIncrement; // 更新角度
            angle = angle % (2 * Math.PI); // 当角度达到2π时重置为0
            requestAnimationFrame(update); // 请求下一帧
        }

        update();
    </script>
</body>
</html>

{% endraw %}
```

