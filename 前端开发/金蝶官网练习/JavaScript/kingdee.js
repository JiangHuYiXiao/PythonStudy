// 1、校验input输入是否为空

//查找提交需求按钮
var sumbitEle = document.getElementById("sumbit");
//查找姓名输入框
var usernameEle = document.getElementById("username");
//查找电话输入框
var cellphoneEle = document.getElementById("cellphone");
//查找姓名输入框下面的div
var user_needEle = document.getElementsByClassName("user_need");

//查找电话号码下面的div
var cell_needEle = document.getElementsByClassName("cell_need");

// 给提交需求按钮绑定事件
sumbitEle.onclick = function () {
    //对姓名输入框取值
    if (usernameEle.value.trim().length === 0) {
        //  显示姓名输入框下面的div
        user_needEle[0].classList.remove("hide")
    }
    if (cellphoneEle.value.trim().length === 0) {
        //  显示姓名输入框下面的div
        cell_needEle[0].classList.remove("hide")
    }
    return false;
};


//2、右侧帮助栏js
//查找联系我们的标签
var cell_us_imgEle = document.getElementsByClassName("cell_us_img");
//绑定事件
cell_us_imgEle[0].onmouseover = function () {


};



// 3、金蝶云，为企业成长而生js

var ycqEle = document.getElementsByClassName("ycq");
ycqEle.onmouseover = function () {

};

