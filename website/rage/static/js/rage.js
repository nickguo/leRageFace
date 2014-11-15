var fn = function(){
    console.log("asdfasdf");
    var wtf = $("#nickyo").val();
    $.get("/rage", {img: wtf}, function(data) {
        $("#image-loc").html("<img src="+data+"/>");
    }); 
};
