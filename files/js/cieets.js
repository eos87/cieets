function mainmenu(){    
    $("#nav ul").css({
        display: "none"
    }); // Opera Fix   
}
$(document).ready(function(){
	//asignar tamaños cuando carga la pagina
	$('.nivel2').each(function(){
    	var ancho = 0;
    	$(this).children().each(function(){
    		ancho = ancho + $(this).width();
    	})
    	$(this).width(ancho);
    });
	//codigo para mostrar el menu
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


