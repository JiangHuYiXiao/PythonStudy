// 1、JavaScript拥有动态类型
var a=123;
var a='abc';
console.log(a);

//2、数值，JavaScript不区分整型和浮点型，就只有一种数字类型。
var b=112;
console.log(b);
// 还有一种NaN，表示不是一个数字（Not a Number）。

// 3、字符串
/*
常用方法：
方法	            说明
.length	        返回长度
.trim()	        移除左右空白
.trimLeft()	    移除左边的空白
.trimRight()	移除右边的空白
.charAt(n)	    返回第n个字符
.concat(value, ...)	        拼接
.indexOf(substring, start)	子序列位置,也就是字符的索引值
.substring(from, to)	    根据索引获取子序列
.slice(start, end)	        切片
.toLowerCase()	            小写
.toUpperCase()	            大写
.split(delimiter, limit)	分割，第一个参数表示根据什么分割，第二个参数表示返回的列表的长度
*/
var c='hello';
console.log(c.length);

var d='  jiang hu  ';
console.log(d.trim());

console.log(c.charAt(3));

console.log(c.concat(d));
console.log(c.concat(1,2));

console.log(d.indexOf('j'));
//表示返回索引位置从1开始到末尾
console.log(d.substring(1));
//表示返回索引位置从3开始到5
console.log(d.substring(3,6));

console.log(d.slice(3,6));
console.log(d.slice(3,-2));
console.log(d.slice(-2,3));


/*
string.slice(start, stop)和string.substring(start, stop)：

两者的相同点：
如果start等于end，返回空字符串
如果stop参数省略，则取到字符串末
如果某个参数超过string的长度，这个参数会被替换为string的长度

substirng()的特点：
如果 start > stop ，start和stop将被交换
如果参数是负数或者不是数字，将会被0替换

silce()的特点：
如果 start > stop 不会交换两者
如果start小于0，则切割从字符串末尾往前数的第abs(start)个的字符开始(包括该位置的字符)
如果stop小于0，则切割从字符串末尾往前数的第abs(stop)个字符结束(不包含该位置字符)
*/
var e='abcaJaT';
console.log(e.toLowerCase());
console.log(e.toUpperCase());
console.log(e.split('a',3));
console.log(e.split('a',4));
console.log(e.split('a',5));