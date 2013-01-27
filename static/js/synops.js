
// OMG, browser sniffing is wrong (but Firefox is doing weird things with bold webfonts)
/*if($.browser.mozilla){
    console.log("Its a Gecko based browser : applying ugly patch to CSS for letter-spacing.");
    $(document).ready(function(){
        $("body").addClass("letter-space-please");
    });
}*/

var timeout_change1 = null;
var timeout_change2 = null;

if (!Array.prototype.indexOf) {
    Array.prototype.indexOf = function (searchElement /*, fromIndex */ ) {
        "use strict";
        if (this == null) {
            throw new TypeError();
        }
        var t = Object(this);
        var len = t.length >>> 0;
        if (len === 0) {
            return -1;
        }
        var n = 0;
        if (arguments.length > 1) {
            n = Number(arguments[1]);
            if (n != n) { // shortcut for verifying if it's NaN
                n = 0;
            } else if (n != 0 && n != Infinity && n != -Infinity) {
                n = (n > 0 || -1) * Math.floor(Math.abs(n));
            }
        }
        if (n >= len) {
            return -1;
        }
        var k = n >= 0 ? n : Math.max(len - Math.abs(n), 0);
        for (; k < len; k++) {
            if (k in t && t[k] === searchElement) {
                return k;
            }
        }
        return -1;
    }
}

function changeTo(id){
    var next = $(".carton[data-cartonid=\"" + id +  "\"]");
    var current = $(".carton.selected");

    if(timeout_change1) window.clearTimeout(timeout_change1);
    if(timeout_change2) window.clearTimeout(timeout_change2);

    current_id = id;

    var $carton = $(".carton");

    if($carton.length > 1){
        next.addClass("next").removeClass('up');

        $(".refcarton").removeClass("selected").closest('.jour').removeClass('selected');
        $(".refcarton[data-cartonid=" + id +  "]").addClass("selected").closest('.jour').addClass('selected');

        current.removeClass('up');
        timeout_change1 = window.setTimeout(function(){
            current.removeClass("selected");
            next.removeClass("next").addClass("selected");
            timeout_change2 = window.setTimeout(function(){
                    next.addClass('up');
                }, 1000);
        }, 250);
    }else{
        $carton.addClass("selected").addClass("up");
    }
}

var current_id = 0;
var change_interval = null;
var carton_ids = [];

function nextCarton(){
    var currentIndex = carton_ids.indexOf(parseInt(current_id, 10));
    var newIndex = 0;

    console.log("Current idx > " + currentIndex);

    if(currentIndex + 1 < carton_ids.length) {
        newIndex = currentIndex + 1;
    }

    console.log("  New index > " + newIndex + " = " + carton_ids[newIndex]);

    var nextone = $(".refcarton[data-cartonid=" + carton_ids[newIndex] + "]");
    if(!nextone.length){
        nextone = $(".refcarton:first");
    }

    changeTo(nextone.attr("data-cartonid"));
    console.log("Current_id > " + current_id)
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

    var $refcarton = $(".refcarton");

    $refcarton.each(function() {
        var cid = parseInt($(this).data("cartonid"), 10);

        if(carton_ids.indexOf(cid) === -1) {
            carton_ids.push(cid);
        }
        console.log(carton_ids);
        console.log(carton_ids.length);
        console.log(carton_ids.indexOf(cid));
    });

    if($(".carton.highlighted").length){
        changeTo($(".carton.highlighted:first").data("cartonid"));
    }else{
        changeTo($(".refcarton:first").attr("data-cartonid"));
    }

    resetChangeInterval();

    $refcarton.click(function(){
       changeTo($(this).data("cartonid"));

       resetChangeInterval();
    });
});