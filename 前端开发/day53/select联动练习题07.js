//找到select标签
var d1Ele = document.getElementById("s1");
//定义一个字典存储省份的值和区的值
var data1 = {1:["宝安区","南山区","福田区"],2:["萍乡","南昌","九江"]};

//绑定改变事件
d1Ele.onchange = function () {
  //  获取省份的值
    var va = this.value;
  //  获取省份下的市区
    var areas = data1[this.value];

  // 获取s2标签
    var s2Ele = document.getElementById("s2");
    //清空之前的option的值
    s2Ele.innerHTML="";
    //创建option标签
    for(i=0;i<areas.length;i++){
        var opEle = document.createElement("option");
        opEle.innerText=areas[i];
        //添加子标签到s2中
        s2Ele.appendChild(opEle);
    }
};