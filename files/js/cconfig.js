$(document).ready(function(){    
    $("#tabs").tabs();

    $("a[rel=example_group]").fancybox({
        'transitionIn'	: 'elastic',
        'transitionOut'	: 'elastic',
        'overlayColor': '#000',
        'titlePosition': 'over',
        'titleFormat': function(title, currentArray, currentIndex, currentOpts) {
            return '<span id="fancybox-title-over">Image ' + (currentIndex + 1) + ' / ' + currentArray.length + (title.length ? ' &nbsp; ' + title : '') + '</span>';
        }
    });
});
jQuery(window).load(function(){
    $("#carrusel-container").carousel( {
        dispItems: 3,
        loop: 'true',
        prevBtn: '<div class="carrusel-button-prev" id="#mycarousel-prev"></div>',
        nextBtn: '<div class="carrusel-button-next" id="#mycarousel-next"></div>',
        btnsPosition: 'outside'
    });
});
