/*1、样式操作
addClass();// 添加指定的CSS类名。
removeClass();// 移除指定的CSS类名。
hasClass();// 判断样式存不存在
toggleClass();// 切换CSS类名，如果有就移除，如果没有就添加。*/

console.log($("#l1"));
$("li").addClass("hide");

$("#l2").removeClass("hide");

console.log($("#l2").hasClass("hide"));

$("#l3").toggleClass("hide");
$("#l2").toggleClass("hide");
