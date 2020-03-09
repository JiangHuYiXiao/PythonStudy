// 1、js操作class
var dEle =document.getElementsByTagName("div");
console.log(dEle);      //返回一个数组
console.log(dEle[0]);   //通过索引获取数组的元素
console.log(dEle[0].className);     // 获取class属性，为字符串
console.log(dEle[0].classList);        // 转换成字典的形式

// dEle[0].classList.remove('c1');         //删除类
// console.log(dEle[0].className);
// dEle[0].classList.add("c0");         //添加类
// console.log(dEle[0].className);
//
// // classList.contains(cls)  存在返回true，否则返回false
// console.log(dEle[0].classList.contains('c1'));
// console.log(dEle[0].classList.contains('c0'));

// toggle应用，切换
// // classList.toggle(cls)  存在就删除，否则添加
// dEle[0].classList.toggle('c1');
// console.log(dEle[0].className);
// dEle[0].classList.toggle('c1');
// console.log(dEle[0].className);

//通过事件修改样式
// function change(ths) {
//     ths.classList.toggle("c2");

// }

// 2、JS操作CSS属性的规律：
//指定修改样式
// dEle[0].style.backgroundColor='blue';
// 1.对于没有中横线的CSS属性一般直接使用style.属性名即可。如：
dEle[0].style.margin='300px';
dEle[0].style.width='300px';
// dEle[0].style.left
// dEle[0].style.position

// 2.对含有中横线的CSS属性，将中横线后面的第一个字母换成大写即可。如：
// obj.style.marginTop
// obj.style.borderLeftWidth
// obj.style.zIndex
// obj.style.fontFamily