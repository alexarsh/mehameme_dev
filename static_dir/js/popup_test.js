$(function() {
    $("#generate").click(function(e) {
        var canvas = $("#meme_canvas")[0];
        var context = canvas.getContext("2d");
        var x = canvas.width / 2;
        var y_top = canvas.height / 10;
        var y_bottom = canvas.height / 1.1;
        context.lineWidth=1;
        context.fillStyle="white";
        context.lineStyle="white";
        context.font="18px bold sans-serif";
        context.textAlign = 'center';
        context.fillText($("#top_text").val(), x, y_top);
        context.fillText($("#bottom_text").val(), x, y_bottom);
    })
    $("#save").click(function(e) {
        var canvas = $("#meme_canvas")[0];
        var strMime = "image/jpeg";
        var strDownloadMime = "image/octet-stream";
        var strData = canvas.toDataURL(strMime);
        strData = strData.replace(strMime, strDownloadMime);
        document.location.href = strData;
    })
});