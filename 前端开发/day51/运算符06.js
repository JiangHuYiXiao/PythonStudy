// 1、算数运算符(+ - * / % ++ --)
var a=10;
var b=3;
// console.log(a+b);
// console.log(a-b);
// console.log(a/b);
// console.log(a%b);       //取余
// console.log(a++);       //+1
// console.log(a);
// console.log(a--);       //-1
// console.log(a);

//2、比较运算符(> >= < <= != == === !==)

console.log(a>b);
console.log(a>=b);
console.log(a<=b);
console.log(a!=b);
console.log(10=='10');          //弱等于，只判断值
console.log(10==='10');         //强等于，值和类型都要判断


//3、逻辑运算符(&& || !)
console.log(1>2&&6>3);      //与
console.log(1>2||6>3);     //或
console.log(!false);     //非

//4、赋值运算符(= += -= *= /=)
var c=3;
console.log(c=4);
console.log(c);
console.log(c += 3);            //c=c+3
console.log(c);
console.log(c -= 3);            //c=c-3
console.log(c);
console.log(c *= 3);            //c=c*3
console.log(c);
console.log(c /= 3);            //c=c/3
console.log(c);
