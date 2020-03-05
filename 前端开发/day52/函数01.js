
//1、函数定义
function foo(a,b) {
    console.log('a:',a);
    console.log('b:',b);
    return(a+b)
}

//2、函数调用
res=foo(11,22);
console.log(res);


//3、匿名函数
var foo2 = function(a,b){
    console.log('a;',a);
    console.log('b;',b);
    return(a+b)
};

res2 = foo2(11,21);
console.log(res2);

// 4、立即执行函数
(function (a,b) {
    console.log('立即执行函数');
    console.log(a+b);
})(11,22);
console.log('===============');

// 5、作用域
(function (a,b) {
    console.log('立即执行函数2');
    console.log(a+b);
    var inner='hello world'
})(11,22);
console.log('===============');
// console.log(inner);  在函数外面不能使用函数内部的变量

// 6、js中形参和实参数量不一致时也可以运行
// 比如说形参只有两个，实参有三个
function foo3(a,b) {
    console.log('a:',a);
    console.log('b:',b);
    return(a+b)
}
res3=foo3(11,22,33);
console.log(res3);

// 比如说形参只有两个，实参有一个
res4=foo3(11);
console.log(res4);


// a: 11
// 函数01.js:43 b: undefined
// 函数01.js:51 NaN



// 7、arguments，多个参数类似与*args
function add(a,b) {
    console.log(a);
    console.log(b);
    console.log(arguments);
    console.log(arguments.length);
    ret=0;
    for (var i=0;i<arguments.length;i++){
        ret +=arguments[i];
    }
    return(ret);
}
console.log(add(11,12));


// 8、局部变量、全局变量、变量生命周期
// 局部：函数内部变量
// 全局：函数外部变量
// 生命周期：
// 全局变量在窗口关闭后删除
// 局部变量在函数运行后删除

// 9、作用域
//首先在函数内部查找变量，找不到则到外层函数查找，逐步找到最外层。

// 示例1：
var city = "BeiJing";
function f() {
  var city = "ShangHai";
  function inner(){
    var city = "ShenZhen";
    console.log(city);
  }
  inner();
}
// 调用
f();


// 示例2：
var city = "BeiJing";
function Bar() {
  console.log(city);
}
function f() {
  var city = "ShangHai";
  return Bar;
}
var ret = f();
// 调用
ret();


// 示例3：
var city = "BeiJing";
function f(){
    var city = "ShangHai";
    function inner(){
        console.log(city);
    }
    return inner;
}
var ret = f();
// 调用
ret();


// 10、词法分析
// JavaScript中在调用函数的那一瞬间，会先进行词法分析。当函数调用的前一瞬间，会先形成一个激活对象：Avtive Object（AO）

// 1、先看是否有参数，如果有，则将此参数赋值给AO，且值为undefined。没有就不做任何操作
// 2、再看是否有局部变量，如果AO上有同名的值，则不做任何操作。如果没有，则将此变量赋值给AO，并且值为undefined。
// 3、函数声明，如果AO上有，则会将AO上的对象覆盖。如果没有，则不做任何操作。

// 示例1：
var age = 18;
function foo(){
  console.log(age);
  var age = 22;         // AO.age=undefined
  console.log(age);
}
foo();


var age = 18;
function foo(){
  console.log(age);
  var age = 22;          // AO.age=undefined
  console.log(age);
  function age(){     // AO.age=function
    console.log("呵呵");
  }
  console.log(age);
}
foo();  // 执行后的结果是？

/*
* 词法分析过程：
1、分析参数，有一个参数，形成一个 AO.age=undefine;
2、分析变量声明，有一个 var age, 发现 AO 上面已经有一个 AO.age，因此不做任何处理
3、分析函数声明，有一个 function age(){...} 声明， 则把原有的 age 覆盖成 AO.age=function(){...};

最终，AO上的属性只有一个age，并且值为一个函数声明

执行过程：
注意：执行过程中所有的值都是从AO对象上去寻找

1、执行第一个 console.log(age) 时，此时的 AO.age 是一个函数，所以第一个输出的一个函数
2、这句 var age=22; 是对 AO.age 的属性赋值， 此时AO.age=22 ，所以在第二个输出的是 2
3、同理第三个输出的还是22, 因为中间再没有改变age值的语句了
*
* */