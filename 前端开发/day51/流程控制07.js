// 1、switch case default
// switch中的case子句通常都会加break语句，否则程序会继续执行后续case中的语句。
var day='1';
switch (day) {
    case '1':
    console.log('麻辣香锅');
    break;
    case '2':
    console.log('水煮鱼');
    break;
    case '3':
    console.log('牛肉火锅');
    break;
    default:
    console.log('吃点啥')

}

// 2、for(定义变量;比较运算;对变量进行操作){循环体}

var a =[10,11,'jianghu','yixiu'];
for(var i=0;i<a.length;i++){
    console.log(i);
    console.log(a[i]);
}


// 3、while 循环
// while (条件) {循环体}
var b=10;
while(b<=18){
    console.log('好好学习js')
    b++;
}

// 4、三元运算
var c = 1;
var d = 2;
var e = c > d ? c : d;          //条件?a:b;   条件成立取值a，条件不成立取值b
console.log(e);



// 5、if else
var hao = 10;
if (hao>9){
    console.log('大于9');
}
else {
    console.log('小于9');
}


// 6、if else if else
var bb=18;
if (bb>18){
    console.log('成年')
}
else if(bb<18){
    console.log('小屁孩')
}
else{
    console.log('刚好')
}