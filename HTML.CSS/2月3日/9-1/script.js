$(function(){
    var sesi = $("#iOndoc").val();
    var kasi = $("#iOndoF").val();
    var kerubin = $("#iOndoc").val();

    $("#iOndoc").on("change",function(){
        sesi = $("#iOndoc").val();
        kasi = sesi * 9/5 + 32
        kerubin = sesi *1 + 273.15;
        $("#iOndoF").val(kasi);
        $("#iOndok").val(kerubin);
    });
    $("#iOndoF").on("change",function(){
        // セ氏温度から華氏温度を計算する
        // セ氏温度から絶対温度を計算する

        $("#iOndoc").val(sesi);
        $("#iOndok").val(kerubin);
    });
    $("#iOndok").on("change",function(){
        //絶対温度からセ氏温度から計算する
        //セ氏温度から華氏温度を計算する
        //セ氏温度の項目を更新する
        //華氏温度の項目を更新する
    })
});
