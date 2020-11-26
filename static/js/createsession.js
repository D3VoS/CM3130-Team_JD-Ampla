$(document).ready(function(){
    $("#sessionbutton").click(function(){
        $(".sessionContainer").css("display", "block");
    });

    $(".close").click(function(){
        $(".sessionContainer").css("display", "none");
    });
});