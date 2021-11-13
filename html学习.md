## 基本标签学习 ##

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>基本标签学习</title>
</head>
<body>
<!--标题标签-->
<h1>一级标签</h1>
<h2>二级标签</h2>
<h3>三级标签</h3>
<h4>四级标签</h4>
<h5>五级标签</h5>
<h6>六级标签</h6>
<!--段落标签-->
<p>静止了，所有的花开</p>
<p>遥远了，清晰了爱</p>
<p>天郁闷，爱却更喜欢</p>
<p>那时候，我不懂</p>
<p>这叫爱，你喜欢</p>
<p>站在那窗台，你好久</p>

<!--水平线标签-->
<hr>

<!--换行标签-->
静止了，所有的花开<br>
遥远了，清晰了爱<br>
天郁闷，爱却更喜欢<br>
那时候，我不懂<br>
这叫爱，你喜欢<br>
站在那窗台，你好久<br>
<!--粗体，斜体-->
<h1>字体样式标签</h1>
粗体： <strong>i love you</strong>
斜体:  <em>i love you</em>
<br>
<!--特殊符号-->
空     格
空&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;格
<br>
&gt;
<br>
&lt;
&copy;版权所有马沈晨
<!--
特殊符号记忆方式


&    ；
-->

</body>
</html>
```

## 图像标签学习 ##

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>图像标签学习</title>
</head>
<body>
<!--
img学习
src：图片地址(必填）
    相对地址（推荐使用），绝对地址
    ../         --上一级目录

alt:图片名字（必填）
-->
<img src="http://r28wqwrna.hn-bkt.clouddn.com/1.png" alt="可爱的胡桃" title="我爱胡桃" width="300" height="300">

<a href="链接标签.html#down">跳转</a>

</body>
</html>
```

## 链接标签 ##

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>链接标签学习</title>
</head>
<body>
<!--a标签
href:必填，表示要跳转到那个页面
target:表示窗口在哪里打开
_blank   在新标签中打开
_self    在自己的网页中打开
-->

<!--使用name作为标记-->
<a name="top">顶部</a>


<a href="firstweb.html" target="_blank">点击我跳转到页面</a>
<a href="http://www.baidu.com">点击我跳转到百度</a>
<br>
<a href="firstweb.html">
    <img src="http://r28wqwrna.hn-bkt.clouddn.com/1.png" alt="可爱的胡桃" title="我爱胡桃" width="300" height="300">
</a>
<br>
<a href="firstweb.html">
    <img src="http://r28wqwrna.hn-bkt.clouddn.com/1.png" alt="可爱的胡桃" title="我爱胡桃" width="300" height="300">
</a>
<br>
<a href="firstweb.html">
    <img src="http://r28wqwrna.hn-bkt.clouddn.com/1.png" alt="可爱的胡桃" title="我爱胡桃" width="300" height="300">
</a>
<br>
<a href="firstweb.html">
    <img src="http://r28wqwrna.hn-bkt.clouddn.com/1.png" alt="可爱的胡桃" title="我爱胡桃" width="300" height="300">
</a>
<br>
<a href="firstweb.html">
    <img src="http://r28wqwrna.hn-bkt.clouddn.com/1.png" alt="可爱的胡桃" title="我爱胡桃" width="300" height="300">
</a>
<br>
<a href="firstweb.html">
    <img src="http://r28wqwrna.hn-bkt.clouddn.com/1.png" alt="可爱的胡桃" title="我爱胡桃" width="300" height="300">
</a>
<br>
<a href="firstweb.html">
    <img src="http://r28wqwrna.hn-bkt.clouddn.com/1.png" alt="可爱的胡桃" title="我爱胡桃" width="300" height="300">
</a>
<br>
<a href="firstweb.html">
    <img src="http://r28wqwrna.hn-bkt.clouddn.com/1.png" alt="可爱的胡桃" title="我爱胡桃" width="300" height="300">
</a>
<br>
<a href="firstweb.html">
    <img src="http://r28wqwrna.hn-bkt.clouddn.com/1.png" alt="可爱的胡桃" title="我爱胡桃" width="300" height="300">
</a>
<br>
<a href="firstweb.html">
    <img src="http://r28wqwrna.hn-bkt.clouddn.com/1.png" alt="可爱的胡桃" title="我爱胡桃" width="300" height="300">
</a>
<br>
<a href="firstweb.html">
    <img src="http://r28wqwrna.hn-bkt.clouddn.com/1.png" alt="可爱的胡桃" title="我爱胡桃" width="300" height="300">
</a>
<!--锚链接
1.需要一个锚标记
2.跳转到标记
#

-->

<a href="#top">回到顶部</a>
<a name="down">down</a>

<!--功能性链接
邮箱链接：mailto
QQ链接
-->

<a href="mailto:704951265@qq.com">点击联系我</a>



</body>
</html>
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>列表学习</title>
</head>
<body>

<!--有序列表
应用范围：试卷，问答...
-->
<ol>
    <li>Java</li>
    <li>Python</li>
    <li>运维</li>
    <li>前端</li>
    <li>C/c++</li>
</ol>

<hr>
<!--无序列表
应用范围：导航，侧边栏。。。
-->
<ul>
    <li>Java</li>
    <li>Python</li>
    <li>运维</li>
    <li>前端</li>
    <li>C/c++</li>
</ul>

<!--自定义列表
dl:标签
dt:列表名称
dd：列表内容
公司网站底部
-->
<dl>
        <dt>学科</dt>

        <dd>Java</dd>
        <dd>Python</dd>
        <dd>Linux</dd>
        <dd>C</dd>
        <dt>位置</dt>
        <dd>湖南</dd>
        <dd>湖北</dd>
        <dd>武汉</dd>
</dl>



</body>
</html>
```

## 表格学习 

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>表格学习</title>
</head>
<body>
<!--表格table
行tr
列td
-->
<table border="1px">
<tr>
<!--colspan 跨列-->
    <td colspan="4">1-1</td>

</tr>
    <tr>
    <td rowspan="2">2-1</td>
    <td>2-2</td>
    <td>2-3</td>
    <td>2-4</td>
    </tr>
    <tr>
        <td>3-1</td>
        <td>3-2</td>
        <td>3-3</td>

    </tr>

</table>


</body>
</html>
```

## 媒体学习 ##

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>媒体元素学习</title>
</head>
<body>
<!--音频和视频
src:资源路径
controls:控制条
autoplay:自动播放
-->
<video src="http://r28wqwrna.hn-bkt.clouddn.com/%E8%83%A1%E6%A1%83%E6%91%87.mp4" controls autoplay muted></video>
<p></p>
<audio src="http://r28wqwrna.hn-bkt.clouddn.com/%E9%9F%B3%E4%B9%90.mp3" controls autoplay ></audio>
</body>
</html>
```

## 页面结构

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>页面结构分析</title>
</head>
<body>
<header>
    <h2>网页头部</h2>
</header>

<section>
    <h2>网页主体</h2>
</section>

<footer>
    <h2>网页脚部</h2>
</footer>
</body>
</html>
```

## 内联框架

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>内联框架学习</title>
</head>
<body>
<!--iframe 内联框架
src :地址
w-h:宽度高度
-->
<iframe src="https://www.Bilibili.com" name="hello" frameborder="0" width="1000px" height="800px"></iframe>

<a href="firstweb.html" target="hello">点击跳转</a>
<!--<iframe src="//player.bilibili.com/player.html?aid=417748849&bvid=BV1YV411J75d&cid=328457276&page=1" -->
<!--        scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>-->
</body>
</html>
```

## 常用的块级元素

```html
address , center , div , dl , form , h1 , h2 , h3 , h4 , h5 , h6 , menu , ol , p , table , ul , li
```

## 常用的内联元素

```html
a , b , br , em , font , img , input , label , select , small , span , textarea 
```


在标准文档流里面，块级元素具有以下特点：

```
①总是在新行上开始，占据一整行；
②高度，行高以及外边距和内边距都可控制；
③宽带始终是与浏览器宽度一样，与内容无关；
④它可以容纳内联元素和其他块元素。
```



每个块元素会按它在HTML标记中出现的顺序依次流入页面，浏览器会自动在每个新的块元素的前后加入一个换行。

若没有设置width，默认宽度为父元素的100%。

当然，块元素可以设置宽高和内外边距，如

```javascript
p{width:800px; height:100px; padding:5px; margin:20px;}
```

效果如下，

![img](https://bbs-img.huaweicloud.com/blogs/img/1593524118840008237.png)

从盒模型原理我们知道，width设置的只是块元素内容区的width，块元素的margin-right默认为auto，会根据内容区的width自动调整，使盒子水平方向上始终平铺整个页面。



内联元素的特点：

```
①和其他元素都在一行上；
②高，行高及外边距和内边距部分可改变；
③宽度只与内容有关；
④行内元素只能容纳文本或者其他行内元素。
```

除了h1、p和div之外，p中还包含**<span>**，div中包含**<a>**，如<span>、<a>这些称为内联元素。以p中包含的元素为例

![img](https://bbs-img.huaweicloud.com/blogs/img/1593527308979008580.png)

内联元素特点是不会自动换行，而是和父元素的文本一起按HTML中的顺序，从左上方流入右下方，p里面的文本可以看做是一种特殊的内联元素（如text1和text2），和其他内联元素（如span)在水平方向上挨着摆放，如果浏览器窗口变窄或设置了width属性，一行放不下，后面的内容就会自动流入下一行，直到所有的子元素都显示在页面上为止。如果父元素p没有设置height，它的height会随浏览器变窄而增高，以保证能放得下所有的内容。

可以设置一下内联元素span的宽和高，看是否有效？

```javascript
p span{width: 100px; height: 100px;padding: 5px;margin: 10px;}
```

渲染效果

![img](https://bbs-img.huaweicloud.com/blogs/img/1593527609937060671.png)
