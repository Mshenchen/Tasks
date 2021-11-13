## CSS简介

- *CSS* 指的是层叠样式表 (*C*ascading *S*tyle *S*heets)

- CSS 描述了*如何在屏幕、纸张或其他媒体上显示 HTML 元素*

- CSS *节省了大量工作*。它可以同时控制多张网页的布局

- 外部样式表存储在 *CSS 文件*中

  ## CSS 节省了大量工作！

  样式定义通常保存在外部 .css 文件中。

  通过使用外部样式表文件，您只需更改一个文件即可更改整个网站的外观！



## CSS语法

CSS 规则集（rule-set）由选择器和声明块组成：

![CSS 选择器](https://www.w3school.com.cn/i/css/selector.gif)

选择器指向您需要设置样式的 HTML 元素。

声明块包含一条或多条用分号分隔的声明。

每条声明都包含一个 CSS 属性名称和一个值，以冒号分隔。

多条 CSS 声明用分号分隔，声明块用花括号括起来。

在此例中，所有 <p> 元素都将居中对齐，并带有红色文本颜色：

```
p {
  color: red;
  text-align: center;
}
```

- p 是 CSS 中的*选择器*（它指向要设置样式的 HTML 元素：<p>）。
- color 是属性，red 是属性值
- text-align 是属性，center 是属性值

## CSS选择器

CSS 选择器用于“查找”（或选取）要设置样式的 HTML 元素。

CSS选择器的四类：

- 三种基本选择器
- 层次选择器
- 结构伪类选择器
- 属性选择器

### 三种基本选择器

#### 标签选择器

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        /* 标签选择器，选择页面上所有这个元素的标签*/
        h1{
            color: red;
            background: yellow;
            border-radius: 21px;
        }
        p{
            font-size: 70px;
        }
    </style>

</head>
<body>
<h1>学习学习</h1>
<h1>摸鱼摸鱼</h1>
<p>EDG加油</p>
</body>
</html>
```

#### 类选择器

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
/* 类选择器的格式*/
    .a{
        color: red;
    }
    .b{
        color: yellow;
    }

    </style>

</head>
<body>
<h1 class="a">标题1</h1>
<h1 class="b">标题2</h1>
<h1 class="a">标题3</h1>
</body>
</html>
```

#### id选择器

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        /*
        id选择器：id必须保证全局唯一
        #id名称{}
        不遵循就近原则
        id选择器>class选择器>标签选择器
        */
    </style>
</head>
<body>
<h1></h1>
</body>
</html>
```

### 层次选择器

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
       /* p{
            background: red;
        }*/
       /*后代选择器*/
       /*body p{
           background: yellow;
       }*/
       /*子选择器*/
        body>p{
            background: green;
        }
       /*相邻兄弟选择器 只有一个，相邻向下*/
       /*.active+p{
           background: green;
           }*/
       /* 通用兄弟选择器:选中向下的所有兄弟元素
       .active~p{
       background :green;}
       */
    </style>
</head>
<body>
<p>p1</p>
<p>p2</p>
<p>p3</p>
<ul>
    <li>
        <p>p4</p>
    </li>
    <li>
        <p>p5</p>
    </li>
    <li>
        <p>p6</p>
    </li>
</ul>

</body>
</html>
```

### 结构伪类选择器

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        /*ul的第一个元素*/
        ul li:first-child{
            background: green;
        }
        /*ul的最后一个元素*/
        ul li:last-child{
            background: yellow;
        }
        a:hover{
            background: red;
        }

    </style>
</head>
<body>
<a href="">321123</a>
    <p>p1</p>
    <p>p2</p>
    <p>p3</p>
    <ul>
        <li>li1</li>
        <li>li2</li>
        <li>li3</li>
    </ul>
</body>
</html>
```

### 属性选择器

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .demo a{
            float: left;
            display: block;
            height: 50px;
            width: 50px;
            border-radius: 10px;
            background: green;
            text-align: center;
            color: gainsboro;
            margin-right: 5px;
        }
        /*属性名，
        = 绝对等于
        *=包含这个元素
        ^=以这个开头
        $=以这个结尾
        */
        a[class*="links"]{
            background: yellow;
        }
    </style>
</head>

<body>
<p class="demo">
    <a href="http:www.baidu.com" class="links item first" id="first">1</a>
    <a href="image" class="links item active" title="test">2</a>
    <a href="image/123" class="links item" >3</a>
    <a href="image/123.jpg" class="links item" >4</a>
    <a href="abc" class="links item active" >5</a>
    <a href="abcd" class="links item last" >6</a>

</p>
</body>
</html>
```

## CSS字体大小

font-size 属性设置文本的大小。

在网页设计中，能够管理文本大小很重要。但是，不应使用调整字体大小来使段落看起来像标题，或是使标题看起来像段落。

请始终使用正确的 HTML 标签，例如 <h1> - <h6> 用于标题，而 <p> 仅用于段落。

font-size 值可以是绝对或相对大小。

绝对尺寸：

- 将文本设置为指定大小
- 不允许用户在所有浏览器中更改文本大小（可访问性不佳）
- 当输出的物理尺寸已知时，绝对尺寸很有用

相对尺寸：

- 设置相对于周围元素的大小
- 允许用户在浏览器中更改文本大小

如果您没有指定字体大小，则普通文本（如段落）的默认大小为 16px（16px = 1em）。

## CSS盒子模型

所有 HTML 元素可以看作盒子，在 CSS 中，"box model "这一术语是用来设计和布局时使用。 

CSS 盒模型本质上是一个盒子，封装周围的 HTML 元素，它包括：边距，边框，填充，和实际内容。

盒模型允许我们在其它元素和周围元素边框之间的空间放置元素。

下面的图片说明了盒子模型 (Box Model)：![CSS box-model](https://7n.w3cschool.cn/statics/images/course/box-model.gif)

content（内容）就是盒子里装的东西，padding（内边距）就是怕盒子里装的东西损坏而添加的泡沫或者其他抗震防挤压的辅料，border（边框）就是盒子本身了，margin（外边距）则说明盒子摆放的时候不能全部堆在一起，要留一定空隙。

在网页设计中，content常指文字、图片等元素，但是也可以是小盒子（DIV嵌套），padding只有宽度属性，可以理解为真实盒子中抗震辅料的厚度，而border有大小和颜色之分，又可以理解为真实盒子的厚度以及这个盒子的颜色或材料，margin就是该盒子与其他东西要保留多大距离，如图所示：

一个盒子实际所占有的宽度（或高度）是由“内容+内边距+边框+外边距”组成的。在CSS中可以通过设置width和height的值来控制内容所占矩形的大小，并且对于任何一个盒子，都可以分别设定4条边各自的border、padding和margin，如下图所示。因此只要利用好这些属性，就能够实现各种各样的排版效果。

## 常用CSS样式

设置元素空间样式：

- width——设置元素的宽度
- height——设置元素的高度
- marin——设置外边距
- padding——设置内填充
- border——给元素盒子添加边框

```html
div{
        width: 100px;    /* 盒子宽100px */
        height: 100px;    /* 盒子高100px */
        margin: 50px;      /* 四周外边距50px */
        /* 为复合样式  margin-right/left/top/buttom：单独设置右边/左边/顶部/底部的外边距 */
        /* margin: 0 50px    填写2个值时，第一个表示上下，第二个表示左右*/
        /* margin：0 4px 5px 6px  填写4个值时，表示顺序为：上 右 下 左 */
        padding: 50px;    /* 四周内填充50px */
        /* 为复合样式  分部样式同margin */
        border: 1px solid black;   /* 四周边框大小为1px 实线 黑色 */
        /* 复合样式   border-width  border-style  border-color  顺序不能乱 */
        background-color: lightblue;
        
    }
```



设置元素内文本的样式：

- font-size——设置字体的大小
- font-weight——设置字体是否加粗（bold—加粗/normal—正常）
- font-style——设置字体形式（italic—倾斜/normal—正常）
- font-familly——设置字体（常用：“微软雅黑”“宋体”）
- line-hight——设置行高 （复合样式写法：font：style weight size/line-height familly）
- color——设置字体颜色
- text-align——设置文本对齐方式（center—居中对齐/left—向左对齐/right—向右对齐）
- text-indent——设置首行缩进距离
- text-decoration——设置文本修饰（underline—文本下添加下划线/line-througn—删除线/overline—上划线/）
- letter-spacing——设置字母间的间距
- word-spacing——设置词间距

```html
div{
        width: 200px;
        height: 25px;

        background-color: lightblue;

        font-size: 15px;   /* 字体大小为15px */
        font-weight: bold;    /* 字体加粗 */
        font-family: "宋体";    /* 字体为宋体 */
        font-style: italic;     /* 字体为斜体 */
        line-height: 25px;     /* 行高为25px，当行高和盒子高度一样是，文本会上下居中 */
        /* 复合样式: 字体大小、行高和字体不能省略，其余可省略不写 */
        /* font: italic bold 15px/25px "宋体" */
        color: red;
        text-align: center;    /* 文本居中 */
    }
```



设置元素盒子背景的样式：

- background-color——设置背景颜色
- background-image——引入一张照片作为背景
- background-repeat——背景图片是否平铺（no-repeat—不平铺）
- background-position——设置背景图片位置
- background-attachment——背景图像是否固定或者随着页面的其余部分滚动。

```html
div{
        width: 300px;
        height: 300px;
        background-color: lightblue;      /* 背景颜色 这是背景颜色不影响引入背景图片 */
        background-image: url(../img.jpg);   /* 引入图片，url()里填入的是图片的地址 */
        background-repeat: no-repeat;    /* 不平铺 */
        background-position: 50px 50px;   /* 图片上左分别移动20px */
        background-attachment: fixed;   /* 图片固定 */
        /* 复合样式  color、repeat、fixed、center可省略*/
        /* background: lightblue url(../img.jpg) no-repeat fixed center  */
    }
```

## CSS常用布局

[CSS常用布局学习记录](https://cloud.tencent.com/developer/article/1389039?from=article.detail.1498806)