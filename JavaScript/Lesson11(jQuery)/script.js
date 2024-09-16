// jQuery(document).ready(function(){код...})
// $(document).ready(function())
// $(".block").addCalss('active');

/*
$(function() {
    $(.nav-menu).attr('data-text', 'Text Block');
})
*/

/*
$(() => {
    $(.nav-menu).attr('data-text', 'Text Block');
})
*/

$("#date-now").text(new Date().getFullYear());
$(":header").css("background", "gray");
// $("#btn1").on("click", () => print());
// $("#btn1").off("click", () => print());

let textAnim = ["111", "222", "333", "444", "555"];
let textId = null;
let textIndex = 0;

function STOP() {
  $("#text-change").text("");
  $(this).next().removeClass("fromTopToDown");
  clearInterval(textId);
  $("#start-stop").text("!").off("click", SAT).on("click", STOP);
}

function SAT() {
  $(this).next().addClass("fromTopToDown");
  textId = setInterval(function () {
    $("#text-change").text(textAnim[textIndex]);
    textIndex = textIndex === textAnim.length - 1 ? 0 : textIndex + 1;
  }, 1000);
  $("#start-stop").html("&times;").off("click", SAT).on("click", STOP);
}

$("#start-stop").on("click", SAT);
