// console.log($("#a1"));
// $(".ycq").hover(
//     function () {
//         console.log($(this).has("#a1"));
//     },
//     function () {
//         $(this).addClass("hide");
//
//     });


// 校验input输入是否为空
$inputEle = $(":text");
$("#sumbit").click(function () {
    console.log($inputEle[0]);
    // for (var i=0;i<$inputEle.length;i++){
    //     if ($inputEle[i].val().trim().length===0){
    //         var name = $inputEle.attr(name);
    //         var html="<div>name不能为空</div>";
    //         $inputEle.after(html)
    //     }
    // }
return false;
});


    // $("#b1").click(function () {  /*找到b1*/
    //     var $needEles = $(".need");/*找到need赋值给$needEles*/
    //     for (var i=0;i<$needEles.length;i++){
    //         if ($($needEles[i]).val().trim().length === 0) {
    //             /*赋值labelName是用户名和密码这两个词*/
    //                                             /*找父类的文本去空格去冒号*/
    //             var labelName = $($needEles[i]).parent().text().trim().slice(0,-1);/*去掉冒号*/
    //             /* 用户名下面的内容就是文本框，添加一个内容***不能为空*/
    //             $($needEles[i]).next().text( labelName +"不能为空!");
    //         }
    //     }
    //     return false;/*提交按钮有自动提交的功能，写这句话就是为了不提交*/
    // })

