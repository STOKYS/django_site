$(".box-click").click(function(){
    console.log(`${$(this).attr("data-type")}: ${$(this).attr("data-id")}`)

});