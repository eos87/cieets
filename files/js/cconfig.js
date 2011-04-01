function mycarousel_initCallback(carousel) {
    $('#mycarousel-next').click(function() {
        carousel.next();
        return false;
    });
    $('#mycarousel-prev').click(function() {
        carousel.prev();
        return false;
    });
};
$(document).ready(function(){
    $("#fotocarrusel").jcarousel({
        scroll: 5,
        initCallback: mycarousel_initCallback,
        buttonNextHTML: null,
        buttonPrevHTML: null
    });
});