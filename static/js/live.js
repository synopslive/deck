var cachedEpisode = {};

function updateWithEpisode(episode) {
    var time = moment(episode.time),
        end_time = moment(episode.end_time),
        now = moment();

    $(".off-synopsis").show();
    $(".synopsis").hide();

    if (time.isAfter(now)) {
        var minutes = time.diff(now, 'minutes');

        if (minutes > 90) {
            var hours = time.diff(now, 'hours');

            $(".live-now-legend").text("Dans " + hours + " heures");
        } else {
            $(".live-now-legend").text("Dans " + minutes + " minutes");
        }
    } else {
        if(end_time.isAfter(now)) {
            $(".live-now-legend").text("Actuellement en direct");
        } else {
            $(".live-now-legend").text("Précédemment");
        }
    }

    if (episode.show_name !== cachedEpisode.show_name) {
        $(".live-show-name").text(episode.show_name);
    }

    if (episode.bg_image !== cachedEpisode.bg_image) {
        $(".live-background").css({
            background: "url(" + episode.bg_image + ") center top"
        }).fadeIn();
    }

    if (episode.content !== cachedEpisode.content) {
        $(".synopsis").html(episode.content);
    }

    if (episode.twitter_widget !== cachedEpisode.twitter_widget) {
        $(".twitter-feed").html(episode.twitter_widget);
        twttr.widgets.load();
    }

    cachedEpisode = episode;
}

function updateWithNothing () {
    $(".live-now-legend").text("Actuellement");
    $(".live-show-name").text("Flux permanent");
    $(".synopsis").hide();
    $(".off-synopsis").show();
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

$(document).ready(function(){
    var liveBackground = $('<div class="live-background"></div>');
    liveBackground.hide();
    $("body").prepend(liveBackground);

    fetchAndUpdate();

    var playing = false;
    var liveAudio = $("#live-audio").clone();
    var currentLiveAudio = null;
    $("#live-audio").remove();

    $(".live-play-button").click(function() {
        if (!playing) {
            currentLiveAudio = liveAudio.clone();
            currentLiveAudio.appendTo(".live-player");

            currentLiveAudio.on('canplaythrough', function(e) {
                currentLiveAudio.get(0).play();
                $(".live-play-button").html('<i class="fa fa-fw fa-pause"></i>');
                $(".live-hint-click").stop(true, true).fadeOut(200);
                $(".live-metadata").fadeIn(2000);
                playing = true;
            });

            $(".live-hint-click").fadeOut(500);

            currentLiveAudio.get(0).preload = "auto";
            currentLiveAudio.get(0).load();
            $(".live-play-button").html('<i class="fa fa-fw fa-spinner fa-spin"></i>');
        } else {
            currentLiveAudio.get(0).src = "";
            currentLiveAudio.get(0).load();
            delete currentLiveAudio.get(0);
            currentLiveAudio.remove();
            playing = false;
            $(".live-metadata").fadeOut(500, function() {
                if (!playing) {
                    $(".live-hint-click").fadeIn(2000);
                }
            });
            $(".live-play-button").html('<i class="fa fa-fw fa-play"></i>');
        }
    });
});