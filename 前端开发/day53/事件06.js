// 1、事件的步骤
    // 1、浏览器上有标签可以点击
    // 2、标签会触发一个点击事件
    // 3、事件需要有函数来处理

// 2、常用事件
// onclick      点击事件
// onfocus      获取焦点                     应用场景：用于表单验证,用户离开某个输入框时,代表已经输入完了,我们可以对它进行验证.
// onblur       失去焦点
// onchange     改变事件                     应用场景：通常用于表单元素,当元素内容被改变时触发.（select联动）
// onkeydown    某个键盘按键被按下。          应用场景: 当用户在最后一个输入框按下回车按键时,表单提交.

// 3、绑定事件的方式

// 方式1：
function changeColor(ths){
    ths.style.backgroundColor="red";

}

// 方式2：

var d2Ele = document.getElementsByClassName("c1");
for (i=0;i<d2Ele.length;i++){
    d2Ele[i].onclick=function () {
    this.style.backgroundColor="blue";
}}

var divEle2 = document.getElementById("d2");
divEle2.onclick=function () {
this.innerText="呵呵";
};

