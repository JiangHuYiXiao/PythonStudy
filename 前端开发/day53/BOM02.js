/*
1、location对象

window.location 对象用于获得当前页面的地址 (URL)，并把浏览器重定向到新的页面。
常用属性和方法：
location.href  获取URL
location.href="URL" // 跳转到指定页面
location.reload() 重新加载页面


// 2、弹出框
//     警告框alert()
//     确认框confirm()
//     提示框prompt()
alert('帅哥');
confirm('你满了18周岁吗？');
prompt('请核对是否正确！');


// 3、计时相关
//通过使用 JavaScript，我们可以在一定时间间隔之后来执行代码，而不是在函数被调用后立即执行。我们称之为计时事件。

// 3.1 setTimeout()
// 语法：
// var t=setTimeout("JS语句",毫秒)
// setTimeout() 方法会返回某个值。在上面的语句中，值被储存在名为 t 的变量中。假如你希望取消这个 setTimeout()，你可以使用这个变量名来指定它。

// setTimeout() 的第一个参数是含有 JavaScript 语句的字符串。这个语句可能诸如 "alert('5 seconds!')"，或者对函数的调用，诸如 alertMsg()"。

// 第二个参数指示从当前起多少毫秒后执行第一个参数（1000 毫秒等于一秒）。

setTimeout("alert('等待5s')",5000);


// 3.2 clearTimeout()
// 语法：
clearTimeout(setTimeout_variable);
// 举个例子：

// 在指定时间之后执行一次相应函数
var timer = setTimeout(function(){alert(123);}, 3000);
// 取消setTimeout设置
clearTimeout(timer);
*/

// 3.3 setInterval()方法可按照指定的周期（以毫秒计）来调用函数或计算表达式。
// setInterval() 方法会不停地调用函数，直到 clearInterval() 被调用或窗口被关闭。由 setInterval() 返回的 ID 值可用作 clearInterval() 方法的参数。

// 语法：
// setInterval("JS语句",时间间隔)
// 返回值
// 一个可以传递给 Window.clearInterval() 从而取消对 code 的周期性执行的值。
// 定时器
function foo(){
    console.log('hh')
}
var t1 = setInterval(foo,1000);

// 3.4 clearInterval()

// clearInterval() 方法可取消由 setInterval() 设置的 timeout。

// clearInterval() 方法的参数必须是由 setInterval() 返回的 ID 值。

// 语法：clearInterval(setinterval返回的ID值)

clearInterval(t1);