jQuery(function() {

var cachedEpisode = {};

function generateTwitterMessageUrl(message) {
    return 'https://twitter.com/intent/tweet?text=' + encodeURIComponent(message);
}

function updateWithEpisode(episode) {
    var time = moment(episode.time),
        end_time = moment(episode.end_time),
        now = moment();

    $(".off-synopsis").hide();
    $(".synopsis").show();

    if (time.isAfter(now)) {
        $(".live-now-legend").text(time.fromNow())
    } else {
        if(end_time.isAfter(now)) {
            $(".live-now-legend").text("Actuellement en direct");
        } else {
            $(".live-now-legend").text("Précédemment");
        }
    }

    if (episode.show_name !== cachedEpisode.show_name) {
        $(".live-show-name").text(episode.show_name);
        $(".show-name").text(episode.show_name);
    }

    if (episode.bg_image !== cachedEpisode.bg_image) {
        var bgImage = $("<img src='' alt='' />").attr("src", episode.bg_image).hide();
        $(".live-background").empty().append(bgImage);
        bgImage.load(function() {
            $(this).fadeIn();
        });
    }

    if (episode.number !== cachedEpisode.number) {
        $(".episode-number").html("#" + episode.number);
    }

    if (episode.content !== cachedEpisode.content) {
        $(".episode-content").html(episode.content);
    }

    if (episode.time !== cachedEpisode.time) {
        $(".episode-time").html(moment(episode.time).format("dddd Do MMMM[, dès ]H[h]mm"));
    }

    if (episode.twitter_widget !== cachedEpisode.twitter_widget) {
        $(".twitter-feed").html(episode.twitter_widget);
        twttr.widgets.load();
    }

    if (episode.twitter_button_label !== cachedEpisode.twitter_button_label) {
        $(".live-post-tweet").html(['<i class="fa fa-fw fa-twitter"></i>', episode.twitter_button_label].join(' '))
    }

    if (episode.twitter_button_message !== cachedEpisode.twitter_button_message) {
        $(".live-post-tweet").attr('href', generateTwitterMessageUrl(episode.twitter_button_message));
    }

    if (episode.copyright !== cachedEpisode.copyright) {
        $(".show-copyright").show();
        $(".show-copyright").html(episode.copyright);
    }

    cachedEpisode = episode;
}

function updateWithNothing () {
    $(".live-now-legend").text("Actuellement");
    $(".live-show-name").text("Flux permanent");
    $(".live-post-tweet").html('<i class="fa fa-fw fa-twitter"></i> SynopsLive');
    $(".live-post-tweet").attr("href", generateTwitterMessageUrl("#SynopsLive"));
    $(".synopsis").hide();
    $(".off-synopsis").show();
    $(".live-background img").fadeOut(function() { $(this).remove(); });
    $(".show-copyright").hide();
}

function updateWithMetadata (data) {
    $(".live-artist").text(data.artist);
    $(".live-album").text(data.title);
}

function fetchAndUpdate() {
    $.getJSON("/feeds/current_episode.json", function(data) {
        if (data.time === undefined || moment(data.time).diff(moment(), 'hours') > 24) {
            updateWithNothing();
        } else {
            updateWithEpisode(data);
        }

        updateWithMetadata(data);
    });

    window.setTimeout(function() {
        fetchAndUpdate();
    }, 10000);
}

function isLivePlaying() {
    var audio = document.querySelector("#live-audio");

    return !audio.paused && !audio.ended && !audio.error;
}

var audio = document.querySelector("#live-audio");

function startAudio() {
    var timeoutLoading = null,
        doneLoading = function(event) {
        clearTimeout(timeoutLoading);
        if (isLivePlaying()) {
            $(".live-play-button").html('<i class="fa fa-fw fa-pause"></i>');
            $(".live-hint-click").stop(true, false).fadeOut(200);
            $(".live-metadata").fadeIn(2000);
        }
    };

    $(audio).on('canplaythrough', doneLoading);
    timeoutLoading = setTimeout(doneLoading, 5000);

    $(".live-hint-click").fadeOut(500);

    if (audio.currentSrc != "") {
        audio.src = [audio.currentSrc.split("?")[0], "?cache=", Date.now()].join("");
    }

    audio.load();
    audio.play();

    $(".live-play-button").html('<i class="fa fa-fw fa-spinner fa-spin"></i>');
}

function stopAudio() {
    var audio = document.querySelector("#live-audio");

    audio.removeAttribute("src");
    audio.load();

    $(".live-metadata").stop(true, false).fadeOut(500, function() {
        if (!isLivePlaying()) {
            $(".live-hint-click").stop(true, false).fadeIn(2000);
        }
    });

    $(".live-play-button").html('<i class="fa fa-fw fa-play"></i>');
}

function toggleAudio() {
    if (isLivePlaying()) {
        stopAudio();
    } else {
        startAudio();
    }
}

function initLive() {
    var liveBackground = $('<div class="live-background"></div>');
    $("body").prepend(liveBackground);

    fetchAndUpdate();

    $(".live-play-button").click(toggleAudio);
}

initLive();

});