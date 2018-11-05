$("input").change(function() {
    $(this).addClass("streched-input");
    $(".unit").addClass("streched-input");
});

$("input").blur(function() {
    $(this).addClass("streched-input");
    $(".unit").addClass("streched-input");
});

var div_list = $("#register-form").find("form").find("div");
var div1 = $(div_list[0]);
var input1 = div1.find("input");
console.log(input1);
input1.removeAttr("autofocus");


$("#id_height").css('padding-right','20px');
$("#id_weight").css('padding-right','20px');

$("#id_height").after("<span class=\"unit\" style=\"margin-left:-30px;\">cm</span>")
$("#id_weight").after("<span class=\"unit\" style=\"margin-left:-30px;\">kg</span>")