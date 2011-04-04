function mainmenu(){
    var elems = $('.nivel2');
    for(var i=0;i<elems.length;i++){
        var ancho = 0;
        var hijos = $(elems[i]).children();
        for(var j=0; j<hijos.length;j++){
            ancho += $(hijos[j]).width();
        }
        $(elems[i]).width(ancho);
    }
    $('.nivel2').each(function(){
        var ancho = 0;
        $(this).children().each(function(){
            ancho += $(this).width();
        });
        $(this).css('width', ancho+'px');
    });
    $("#nav ul").css({
        display: "none"
    }); // Opera Fix
    $("#nav li").hover(function(){
        $(this).find('ul:first').css({
            visibility: "visible",
            display: "none"
        }).show(600);
    },function(){
        $(this).find('ul:first').css({
            visibility: "hidden"
        });
    });
}
$(document).ready(function(){
    mainmenu();    
});
$(window).load(function(){
    var sidebar = $('#sidebar').height();
    var cuerpo = $('#cuerpo').height();
    if(cuerpo>=sidebar){
        $('#sidebar').height(cuerpo);
    }else{
        $('#cuerpo').height(sidebar);
    }
});


