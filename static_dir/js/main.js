var car1;
var car2;
var car3;

$(function()  {
        //define form params
        $( "#dialog-form" ).dialog({
            autoOpen: false,
            height: 400,
            width: 600,
            modal: true,
            buttons: {
                Cancel: function() {
                    $( this ).dialog( "close" );
                }
            },
            close: function() {

            }
        });
        $(".image").click(function(e) {
            var imageUrl = $(this).attr("src");
            var newImageUrl = imageUrl.replace("ready", "empty");
            var can = document.getElementsByTagName('canvas')[0];
            can.style.background = "url(" +newImageUrl + ")";
            can.style.backgroundRepeat = 'no-repeat';
            $( "#dialog-form" ).dialog( "open" );
        });

    }


);
//function addToFirst(imageUrl){
//    //set background
////    var memeCanvas = $("#meme_canvas").css("background-image", "url(/static/images/empty_memes/1.jpg);");
//    alert($(this).attr("src"));
//    var can = document.getElementsByTagName('canvas')[0];
//    can.style.backgroundImage = "url(" +imageUrl + ")";
//    $( "#dialog-form" ).dialog( "open" );
//
//}



