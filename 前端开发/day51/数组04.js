// alert('数组对象的作用是：使用单独的变量名来存储一系列的值。类似于Python中的列表。');
//定义数组
// var a = [1,2,4];
// console.log(a);

// //数组长度
// console.log(a.length);
//
// //尾部追加元素
// console.log(a.push('aa'));
// console.log(a);
//
// //获取尾部元素
// console.log(a.pop());
// console.log(a.pop());
// console.log(a.pop());
//
// //头部添加元素
// console.log(a.unshift('东方红'));
// console.log(a);

//头部清除元素
// console.log(a.shift());
// console.log(a);

//切片
// console.log(a.slice(1,3));

//反转
// console.log(a.reverse());

//将数组元素连接成字符串
// console.log(a.join('+'));

//连接数组
// console.log(a.concat(['a','b','c'],[11,12,13]));

//排序只能按照字符串去比较，比较第一个数，第二个数
// var b=[12,15,23,19,29];
// console.log(b.sort());


// undefined，null的区别
// undefined表示已经声明但是没有赋值，还有就是函数无明确的返回值时，返回的也是undefined。
// null表示值为空


// 布尔值
// js的布尔值是true和false都是小写

// 数组遍历
var b=[12,15,23,19,29];
for (var i=0;i<b.length;i++){
    console.log(b[i]);
}

// 数据类型
var name='xiaogou';
var age=15;
var sex=false;
var student=['xiaogou','nihao','jianghu','hutu'];
var box;
var nu = null;
console.log(typeof name);       //string
console.log(typeof age);        //number
console.log(typeof sex);        //boolean
console.log(typeof student);//object
console.log(typeof box);   //undefined
console.log(typeof nu);     // object



