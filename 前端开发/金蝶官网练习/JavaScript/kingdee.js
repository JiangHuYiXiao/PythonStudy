// console.log($("#a1"));
$(".ycq").hover(
    function () {
        console.log($(this).has("#a1"));
    },
    function () {
        $(this).addClass("hide");

    });