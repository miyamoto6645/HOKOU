function func(x){
    var y = x;
    return y;
}
$(function(){
    $("button").on("click",function (){
        var item = document.getElementById("iCanvas");
        var ctx = item.getContext("2d");
        ctx.style = "black";
        int = 0;
        for (let i =0; i<9; i++){
            console.log(i);
        }
        var x = 0;
        var y = func(x);
        ctx.fillRect(x,y,10,10);
    });
});
