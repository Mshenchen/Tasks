## JavaScript学习

## **1、数据类型**

JavaScript语言的每一个值，都属于某一种数据类型。 JavaScript共有六种数据类型：

```
数值（number）：整数和小数
字符串（string）：字符组成的文本
布尔值（boolean）：true和false两个特定值。
undefined：表示未定义或不存在。
null：表示空缺，即此处应该有一个值，但此时为空。
对象（object）：各种值组成的集合。
```

## **2、typeof运算符**

在JavaScript中，我们可以用typeof运算符来确定一个值到底是什么类型。

（1）原始类型

数值、字符串、布尔值分别返回number、string、boolean。

```
typeof 12  // "number"typeof '12'  // "string"typeof false //"boolean"
```

（2）函数 函数返回function。

```
function a(){}typeof a   // "function"
```

（3）undefined undefined返回undefined。

```
typeof undefined   // "undefined"
```

可用typeof检测一个变量是否声明。

```
if(typeof a === "undefined" ){}
```

（4）其他 除此以外，其他情况都返回object

```
typeof window  // "object"typeof {}  // "object"typeof []  // "object"typeof null // "object"
```

## 3、数值

JavaScript不区分整数值和浮点数值。JavaScript中的所有数字均用浮点数值表示。 JavaScript采用IEEE 754标准定义的64位浮点格式表示数字。

**数值范围**

-9007199254740992 ~ 9007199254740992 

**Infinity**

当JavaScript在算术运算时发生溢出（overflow）、下溢（underflow）或被零整除时不会报错。

当数字运算结果超过了JavaScript所能表示的数字上限（溢出），结果为一个特殊的无穷大（Infinity）值。同样，当负数的值超过了JavaScript所能表示的负数范围，结果为负无穷大（-Infinity）。

**NaN**

NaN用来表示非数字值。

NaN不等于任何值，包括它本身。

```
NaN === NaN  //false
```

## **变量声明**

在JavaScript程序总，使用一个变量之前应当先声明。 变量是使用关键字var来声明的。

```
var a;
a=1;
```

JavaScirpt是一种动态类型语言，也就是说，变量的类型没有限制，可以赋予各种类型的值。 如果只是声明变量而没有赋值，则该变量的值是undefined。undefined是一个JavaScript关键字，表示“无定义”。 如果一个变量没有声明就直接使用，JavaScript会报错，告诉你变量未定义。

## 语句

**if**

```
if(expression)  
{     
	statement;  
}
```

**if..else..**

```
if(expression){
statement1;  
}else{
statement2;  
}
```

**switch**

```
switch(expression){
case "":  statement ;break;    
case "": statement1;break;     
....    
default: statements; break;  
}
```

**和C语言语法极其类似，不多做介绍**

## 对象

对象是单个实物的抽象。

一本书、一辆汽车、一个人都可以是“对象”，一个数据库、一张网页也可以是“对象”。世界上所有的对象都可以是“对象”。

对象是一个容器，封装了“属性”（property）和“方法”（method）。

属性，就是对象的状态，而方法，就是对象的行为。比如：我们可以把一辆汽车抽象成一个对象，它的属性就是它的颜色、重量等，而方法就是它可以启动、停止等。

对象是一种复合值：它将很多值集合在一起，可通过名字访问这些值。对象也可看做一种无序的数据集合，由若干个“键值对”（key-value）构成。 

`var o={ name:'a'}`

上面代码中，大括号定义了一个对象，它被赋值给变量o。这个对象内部包含一个键值对（又称为“成员”），name是“键名”（成员的名称），字符串a是“键值”（成员的值）。键名与键值之间用冒号分隔。如果对象内部包含多个键值对，每个键值对之间用逗号分隔。

在JavaScript中，有三种方法创建对象

```
对象直接量： var o={};
关键字new： var o=new Object();
Object.create()函数： var o=Object.create(null)
```

**读取属性**

读取对象的属性，有两种方法，一种是使用点运算符，还有一种是使用方括号运算符。

```
var o = {  name : 'a'}
o.name  // "a"
o['name']  //"a"
```

JavaScript对象是动态的，可新增属性也可删除属性。但注意，我们是通过引用而非值来操作对象。



### for...in循环用来遍历一个对象的全部属性。

```html
var o = {
  name : 'a',
  age : 12
}
for(var i in o){
  console.log(o[i])
}
// "a"
// 12
```

### 查看所有属性

```html
var o = {
 name : 'a',
 age : 12
}

Object.keys(o)  //['name','age']
```

### 删除属性

### delete运算符可以删除对象的属性。

```javascript
var o={
  name : 'a'
}
delete o.name  //true
o.name  //undefined
```

### 原型

 每一个JavaScript对象（null除外）都和另一个对象相关联，也可以说，继承另一个对象。另一个对象就是我们熟知的“原型”（prototype），每一个对象都从原型继承属性。只有null除外，它没有自己的原型对象。 

 所有通过对象直接量创建的对象都具有同一个原型对象，并可以通过JavaScript代码Object.prototype获得对原型对象的引用。 

 通过关键字new和构造函数调用创建的对象的原型就是构造函数的prototype属性的值。比如：通过new Object()创建的对象继承自Object.prototype；通过new Array()创建的对象的原型就是Array.prototype。 

 没有原型的对象为数不多，Object.prototype就是其中之一，它不继承任何属性。

## 数组

数组是值的有序集合。每个值叫做一个元素，而每个元素在数组中有一个位置，以数字表示（从0开始），称为索引，整个数组用方括号表示。

```
var  arr = [1,2,3];
```

除了在定义时赋值，数组也可以先定义后赋值。

```
var arr = [];arr[0] =1;
```

数组元素可以是任意类型。

```
var arr = [1,'a',{name:'a'},function(){}];
```

上面数组arr的4个元素分别是数字，字符串，对象，函数。

数组属于一种特殊的对象。

```
typeof [1]  // "object"
```

JavaScript语言规定，对象的键名一律为字符串，所以，数组的键名其实也是字符串。之所以可以用数值读取，是因为非字符串的键名会被转为字符串。

### 创建数组

```
var  arr = [1,2,3];
```

length属性是可写的。如果人为设置一个小于当前成员个数的值，该数组的成员会自动减少到length设置的值。

```
var arr = [1,2,3]
arr.length  //3
arr.length = 2;
arr //[1,2]
```

将数组清空的一个有效方法，就是将length属性设为0。

```
var arr = [1,2,3];
arr.length = 0;
arr  //[]
```

如果人为设置length大于当前元素个数，则数组的成员数量会增加到这个值，新增的位置都是空位。

```
var arr = [1];
arr.length=3;
arr[1]  //undefined
```

### 数组元素的添加和删除

可以使用push()方法在数组末尾添加一个或多个元素。

```
var arr = [1,2]
arr.push(3)  // [1,2,3]
arr.push('a','b') //[1,2,3,'a','b']

// shift()是删除数组的一个元素。 
arr.shift()   // [2,3,'a','b']
```

### 多维数组

JavaScript不支持真正的多维数组，但可以用数组的数组来近似。也可以说，数组里放数组。

```
var arr = [[1],[2,3]];
arr[0][0]  // 1
arr[1][1]  //3
```

### 遍历

我们可以使用for循环、while循环、for..in或者forEach()方法来遍历数组

```
var a = [1, 2, 3];   

// for循环 
for(var i = 0; i < a.length; i++) {
console.log(a[i]); 
}

//while
var i = 0;
while (i < a.length) { 
console.log(a[i]);   
i++;
}

//for..in
for (var i in a) { 
console.log(a[i]);  
}

//forEach
a.forEach(function(v){ 
console.log(v);
}
```

在JavaScript中，有些对象被称为“类数组对象”。意思是，它们看上去很像数组，可以使用length属性，但是它们并不是数组，无法使用一些数组的方法。

```
var o = {  0: 'a', 
1: 'b', 
length:2
}
o[0]  // "a"
o[1]  // "b"
o.length // 2
o.push('d') // TypeError: o.push is not a function
```

上面代码中，变量o是一个对象，虽然使用的时候看上去跟数组很像，但是无法使用数组的方法。这就是类数组对象。 

类数组对象有一个特征，就是具有length属性。换句话说，只要有length属性，就可以认为这个对象类似于数组。但是，对象的length属性不是动态值，不会随着成员的变化而变化。