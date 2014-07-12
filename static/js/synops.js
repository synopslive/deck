jQuery(function($) {
    $(".go-antenna").on("click", function(event) {
        $(".menu-shows").slideUp();
        $(".menu-antenna").slideToggle();
        event.preventDefault();
    });
    $(".go-shows").on("click", function(event) {
        $(".menu-antenna").slideUp();
        $(".menu-shows").slideToggle();
        event.preventDefault();
    });
});