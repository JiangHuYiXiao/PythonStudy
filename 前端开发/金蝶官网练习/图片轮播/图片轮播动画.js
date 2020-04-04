
//先获取元素
var box = document.getElementsByClassName("big_box")[0];
var spot = document.getElementsByClassName("spot_list");
var block = document.getElementsByClassName("block")[0];
var left_btn = document.getElementsByClassName("left_btn")[0];
var right_btn = document.getElementsByClassName("right_btn")[0];
var time = null;
var count = 0;

//计时器
function showtime() {
    time = setInterval(function () {
        mate();
    }, 2000);
}
//正常滚动
function mate() {
    box.className = "big_box nav";
    spot[count].style.background = "rgba(255, 255, 255, 0.3)";
    count++;
    spot[count > box.children.length - 2 ? 0 : count].style.background = "rgba(91,91,91,0.8)";
    box.style.marginLeft = (count * -1920) + "px";
    //添加一次性计时器
    setTimeout(function () {
    //判断count的值。如果大于图片长度，就重0开始+
        if (count > box.children.length - 2) {
            count = 0;
            box.className = "big_box";
            box.style.marginLeft = "0px"
        }
    }, 1000)
}
//然后设置鼠标进入计时器关闭，鼠标离开计时器打开
block.onmouseenter = function () {
        clearInterval(time);
    };
    //鼠标出来计时器打开
    block.onmouseleave = function () {
        showtime();
    };
//接下来，来做底下鼠标放在地下图标的时候切换对应的图片。这里我用的是for循环。
for (var i = 0; i < spot.length; i++) {
        spot[i].index = i;
        spot[i].onmouseenter = function () {
            spot[count].style.background = "rgba(255, 255, 255, 0.3)";
            this.style.background = "rgba(91,91,91,0.8)";
            count = this.index;
            box.style.marginLeft = (count * -1920) + "px";
        }

    }

//上面大部分功能已经完成，现在剩下最后一步，左右键切换图片的上一张和下一张。用鼠标点击事件。
// 左边很简单，直接执行开始时候的方法即可（切换方向和自动切换方向相同）。右边用count–
 //图片左边划
right_btn.onclick = function () {
    mate();
};
    //图片右边划
left_btn.onclick = function () {
    spot[count].style.backgroundColor = "rgba(255,255,255,0.3)";
    count--;
    if (count < 0) {
        box.className = "box_big";
        count = box.children.length - 2;
        box.style.marginLeft = "-9600px";
    }
    //添加一次性计时器
    setTimeout(function () {
        box.className = "box_big nav";
        box.style.marginLeft = (-1920 * count) + "px";
        spot[count].style.backgroundColor = "rgba(91,91,91,0.8)";
    }, 1);
};