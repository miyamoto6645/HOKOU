$(function () {
    var sesi = $("#iOndoC").val();
    var kasi = $("#iOndoF").val();
    var kerubui = $("#iOndoK").val();

    $("#iOndoC").on("change", function (){
        sesi = $("#iOndoC").val();
        kasi = sesi * 9/5 +32
        kerubui = sesi*1 +273.15;
        $("#iOndoF").val(kasi);
        $("#iOndoK").val(kerubin);
    });
    $("#iOndoF").on("change",function(){
        //セ氏温度から華氏温度を計算する
        sesi = kasi-32/1.8;
        //セ氏温度から絶対温度を計算する
        kerubin = sesi + 273;
        $("#iOndoC").val(sesi);
        $("#iOndoK").val(kerubin);
    });
    $("#iOndoK").on("change",function (){
        //絶対温度からセ氏温度を計算する
        kerubin = sesi - 273;
        //セ氏温度から華氏温度を計算する
        sesi = kasi-32/1.8;
        //セ氏温度の項目を更新する
         sesi = $("#OndoC").val("UPDATE");
        //華氏温度の項目を更新する
        kasi = $("#OndoC").val("UPDATE");
    });
    