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


/*onclick        当用户点击某个对象时调用的事件句柄。
ondblclick     当用户双击某个对象时调用的事件句柄。

onfocus        元素获得焦点。               // 练习：输入框
onblur         元素失去焦点。               应用场景：用于表单验证,用户离开某个输入框时,代表已经输入完了,我们可以对它进行验证.
onchange       域的内容被改变。             应用场景：通常用于表单元素,当元素内容被改变时触发.（select联动）

onkeydown      某个键盘按键被按下。          应用场景: 当用户在最后一个输入框按下回车按键时,表单提交.
onkeypress     某个键盘按键被按下并松开。
onkeyup        某个键盘按键被松开。
onload         一张页面或一幅图像完成加载。
onmousedown    鼠标按钮被按下。
onmousemove    鼠标被移动。
onmouseout     鼠标从某元素移开。
onmouseover    鼠标移到某元素之上。

onselect      在文本框中的文本被选中时发生。
onsubmit      确认按钮被点击，使用的对象是form。*/
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

