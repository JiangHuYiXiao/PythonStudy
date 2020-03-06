// 1、什么是DOM树：
    // DOM（Document Object Model）是一套对文档的内容进行抽象和概念化的方法。
    // 当网页被加载时，浏览器会创建页面的文档对象模型（Document Object Model）。
    // HTML DOM 模型被构造为对象的树。

// 2、DOM包含哪些？

    // DOM标准规定HTML文档中的每个成分都是一个节点(node)：
    // 文档节点(document对象)：代表整个文档
    // 元素节点(element 对象)：代表一个元素（标签）
    // 文本节点(text对象)：代表元素（标签）中的文本
    // 属性节点(attribute对象)：代表一个属性，元素（标签）才有属性
    // 注释是注释节点(comment对象)　

// 3、JS操作DOM
// 3.1 查找标签
    // 直接查找
console.log(document.getElementById("d3"));
console.log(document.getElementsByClassName("c1"));
console.log(document.getElementsByTagName("div"));

    //间接查找
/*
parentElement            父节点标签元素
children                 所有子标签
firstElementChild        第一个子标签元素
lastElementChild         最后一个子标签元素
nextElementSibling       下一个兄弟标签元素
previousElementSibling   上一个兄弟标签元素

var d5Ele = document.getElementById("d5");
console.log(d5Ele.parentElement);

var d4Ele = document.getElementById("d4");
console.log(d4Ele.children);
console.log(d4Ele.firstElementChild);
console.log(d4Ele.lastElementChild);
console.log(d4Ele.nextElementSibling);
console.log(d4Ele.previousElementSibling);


// 3.2 节点操作
//创建节点createElement
var imgEle = document.createElement("img");     //添加

//添加节点
    // 1、在某个标签内部追加一个子标签
    // somenode.appendChild(newnode)；
    // 2、在某个父标签的内部的另一个标签的前面添加一个子标签
    // somenode.insertBefore(newnode,某个节点);

// 1、在d1标签内部追加一个img标签
var d1Ele = document.getElementById("d1");
d1Ele.appendChild(imgEle);                  // 在d1标签之内插入img标签
imgEle.src="https://gss3.bdstatic.com/7Po3dSag_xI4khGkpoWK1HF6hhy/baike/w%3D268%3Bg%3D0/sign=3a10fbb04b166d22387712927e186eca/6609c93d70cf3bc7f0d6b197d900baa1cc112af2.jpg";        // 标签属性src添加

// 2、在d4内部的第一个子标签前面添加a标签
var aEle=document.createElement("a");
aEle.innerText='百度';
aEle.href="https://www.baidu.com";
var d4Ele = document.getElementById("d4");
var d4SonEle = d4Ele.firstElementChild;
console.log(d4SonEle);
d4Ele.insertBefore(aEle,d4SonEle);

//删除节点
// 语法：获得要删除的元素，通过父元素调用该方法删除。
// somenode.removeChild(要删除的节点)
var s1Ele = document.getElementById("s1");
console.log(s1Ele);
var aEle1 = s1Ele.firstElementChild;
console.log(aEle1);
s1Ele.removeChild(aEle1);


// 替换节点
// somenode.replaceChild(newnode, 某个节点);
var div7Ele = document.createElement("div");
div7Ele.innerText='div7';
div7Ele.id="d7";
var s1Ele = document.getElementById("s1");
console.log(s1Ele);
var aEle1 = s1Ele.firstElementChild;
console.log(aEle1);
s1Ele.replaceChild(div7Ele,aEle1);
*/

//节点属性
// innerText    设置文本内容，获取标签之间的文本内容
// innerHTML  设置标签的内容，获取的是子标签和子标签的内容
var p8Ele = document.createElement("p");
var p9Ele = document.createElement("p");
p8Ele.innerText= '段落1';
p9Ele.innerHTML= '段落2';

var d1Ele = document.getElementById('d1');
d1Ele.appendChild(p8Ele);
d1Ele.appendChild(p9Ele);
console.log(d1Ele.innerText);
console.log(d1Ele.innerHTML);

// 内置属性我们可以使用.id = "d1"进行设置
// 自定义属性只能通过.setAttribute(attribute,value);进行设置
// 自定义属性只能通过.getAttribute(attribute);进行拿值
// 自定义属性只能通过.removeAttribute("age")删除属性

var d1Ele = document.getElementById("d1");
d1Ele.setAttribute("age",19);
console.log(d1Ele.getAttribute("age"));
d1Ele.removeAttribute("age");
console.log(d1Ele.getAttribute("age"));