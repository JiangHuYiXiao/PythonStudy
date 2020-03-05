// 对象后面的点只能跟属性不能跟变量

// JavaScript中所有的事物都是对象：字符串String、数字Number、数组Array、日期等等，对象就是拥有属性和方法的数据。
// JavaScript中的对象实际就是键值对的组合，但是键只能是字符串
/*
// 1、自定义对象
var s1 =[1,2];
var s2 = new Array(1,2);
console.log(s1,typeof(s1));
console.log(s2,typeof(s2));

var name ='abc';
var d1 ={"name":"jianghu","age":"18","abc":"123"};
console.log(typeof(d1));
console.log(d1["name"]);
console.log(d1.name);
console.log(d1.age);


console.log(d1.name);         //对象后面的点只能跟属性不能跟变量
console.log(d1["abc"]);         //对象后面的点只能跟属性不能跟变量

// 创建对象：

var person=new Object();  // 创建一个person对象
person.name="Alex";  // person对象的name属性
person.age=18;  // person对象的age属性
console.log(person,typeof(person));

*/

// 2、Date对象
    // 2.1 创建Date对象
d1 = new Date();
console.log(d1,typeof(d1));   //Thu Mar 05 2020 08:17:41 GMT+0800 (中国标准时间) "object"

    // 2.2 字符串时间
console.log(d1.toLocaleString(),typeof(d1.toLocaleString()));       //2020/3/5 上午8:17:41 string

    // 2.3 有参数的Date对象
d2 = new Date("2020-03-05 12:09:54");
console.log(d2.toLocaleString());           //转成本地字符串时间
console.log(d2.toUTCString());           //转成标准字符串时间 和本地的北京时间差八个小时
console.log(d2);

    // 2.4 Date对象的方法
console.log(d2.getDate());   //获取日
console.log(d2.getDay());   //获取星期
console.log(d2.getFullYear());   //获取长字符串的年
console.log(d2.getHours());   //获取时
console.log(d2.getMinutes());   //获取分
console.log(d2.getSeconds());   //获取秒
console.log(d2.getMonth());   //获取月（0-11）
console.log(d2.getMilliseconds());   //获取毫秒
console.log(d2.getMilliseconds());   //获取毫秒
console.log(d2.getTime());   //获取累计毫秒数(从1970/1/1午夜)开始算起

// 3、Json对象
var str1 = '{"name": "Alex", "age": 18}';
var obj1 = {"name": "Alex", "age": 18};

//把字符串转换成Json对象
console.log(JSON.parse(str1));


//把Json对象转成字符串

console.log(JSON.stringify(obj1));
var1 = JSON.stringify(obj1);
console.log(typeof(var1));
// 4、Math对象

/*
abs(x)      返回数的绝对值。
exp(x)      返回 e 的指数。
floor(x)    对数进行下舍入。
log(x)      返回数的自然对数（底为e）。
max(x,y)    返回 x 和 y 中的最高值。
min(x,y)    返回 x 和 y 中的最低值。
pow(x,y)    返回 x 的 y 次幂。
random()    返回 0 ~ 1 之间的随机数。
round(x)    把数四舍五入为最接近的整数。
sin(x)      返回数的正弦。
sqrt(x)     返回数的平方根。
tan(x)      返回角的正切。
*/

var m1 = new Array(11,22,33);
ret = JSON.stringify(m1);
console.log(m1,typeof(ret));
console.log(m1.length);
console.log(Math.max(m1));      // 这样是获取不到m1的最大值的，因为max方法的参数不能为数组
console.log(Math.max.apply(null,m1));
/*
1.apply()应用某一对象的一个方法，用另一个对象替换当前对象
var max = Math.max.apply(null,arr);
console.log(max)
由于max()里面参数不能为数组，所以借助apply(funtion,args)方法调用Math.max()，function为要调用的方法，args是数组对象，当function为null时，默认为上文,即相当于apply(Math.max,arr)
*/

console.log(Math.min(m1));
console.log(Math.min.apply(null,m1));
console.log(Math.abs(m1[1]));
console.log(Math.random());


// 5、RegExp对象
    //创建正则对象方式1 5.1
// 参数1 正则表达式(不能有空格)
// 参数2 匹配模式：常用g(全局匹配;找到所有匹配，而不是在第一个匹配后停止)和i(忽略大小写)
var reg1 = new RegExp("^[a-zA-Z][a-zA-Z0-9_]{2,6}$");

//RegExp对象的test方法，测试一个字符串是否符合对应的正则规则，返回值是true或false。

console.log(reg1.test("jianghu"));
console.log(reg1.test("jianghuy"));


    //创建正则对象方式2 5.2
console.log(/^[a-zA-Z][a-zA-Z0-9_]{2,6}$/.test("jianghu"));     // true

// 正则表达式注意事项：
// 1、表达式中不能有空格
console.log(/^[a-zA-Z][a-zA-Z0-9_]{2, 6}$/.test('jianghu'));   // false

// 2、当我们不加参数调用RegExpObj.test()方法时, 相当于执行RegExpObj.test("undefined"), 并且/undefined/.test()默认返回true。
console.log(/^undefined$/.test());   // true

// 3、如果regExpObject带有全局标志g，就会出现true和false交替出现,所以我们在使用test()方法校验一个字符串是否完全匹配时，一定要加上^和$符号。
var reg2 = /alex/g;
console.log(reg2.test("alex"));     //true
console.log(reg2.test("alex"));     //false


// 4、全局匹配模式g和不区分小写i
var s2 = 'jianghuaA';
console.log(s2.replace(/a/g,'哈'));      //ji哈nghu哈A
console.log(s2.replace(/a/gi,'哈'));      //ji哈nghu哈哈


// 5、String对象与正则结合的4个方法
var s3 = "hello world";

console.log(s3.match(/o/g));         // ["o", "o"]             查找字符串中 符合正则 的内容
console.log(s3.search(/h/g));        // 0                      查找字符串中符合正则表达式的内容位置
console.log(s3.split(/o/g));         // ["hell", " w", "rld"]  按照正则表达式对字符串进行切割
console.log(s3.replace(/o/g, "s"));  // "hells wsrld"          对字符串按照正则进行替换
