
// OMG, browser sniffing is wrong (but Firefox is doing weird things with bold webfonts)
/*if($.browser.mozilla){
    console.log("Its a Gecko based browser : applying ugly patch to CSS for letter-spacing.");
    $(document).ready(function(){
        $("body").addClass("letter-space-please");
    });
}*/

var timeout_change1 = null;
var timeout_change2 = null;

function changeTo(id){
    var next = $(".carton[data-cartonid=\"" + id +  "\"]");
    var current = $(".carton.selected");
    var tohide = "h1, .tagline, .infos, .social-event, .social-talk";

    if(timeout_change1) window.clearTimeout(timeout_change1);
    if(timeout_change2) window.clearTimeout(timeout_change2);

    current_id = id;

    if($(".carton").length > 1){
        next.addClass("next").removeClass('up');

        $("ul#planning li").removeClass("selected");
        $("ul#planning li[data-cartonid=" + id +  "]").addClass("selected");

        current.removeClass('up');
        timeout_change1 = window.setTimeout(function(){
            current.removeClass("selected");
            next.removeClass("next").addClass("selected");
            timeout_change2 = window.setTimeout(function(){
                    next.addClass('up');
                }, 1000);
        }, 250);
    }else{
        $(".carton").addClass("selected").addClass("up");
    }
}

var current_id = 0;
var change_interval = null;

function nextCarton(){
    var nextone = $("ul#planning li[data-cartonid=" + current_id + "]").next();
    if(!nextone.length){
        nextone = $("ul#planning li:first");
    }

    changeTo(nextone.attr("data-cartonid"));
}

function resetChangeInterval(){
    if(change_interval) window.clearInterval(change_interval);

    change_interval = window.setInterval(
        function(){
            nextCarton();
        }, 12000
    );
}

$(document).ready(function(){
    var len = $(".carton").length;

    if($("#page.home .carton.highlighted").length){
        changeTo($("#page.home .carton.highlighted:first").attr("data-cartonid"));
    }else{
        changeTo($("ul#planning li:first").attr("data-cartonid"));
    }

    resetChangeInterval();

    $("ul#planning li").click(function(){
       changeTo($(this).attr("data-cartonid"));

       resetChangeInterval();
    });
});