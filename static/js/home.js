jQuery(function($) {
    var episodes = $(".calendar-episode"),
        now = moment();

    episodes.each(function() {
       var episode_moment = moment.unix($(this).data('timestamp'));
       if (episode_moment.isBefore(now)) {
           $(this).addClass("in-the-past");
       }
    });

    function showCartonForEpisodeId(episode_id) {
        var old_up = $(".carton");
        var old_selected = $(".carton.selected");
        var target_carton = $(".carton[data-episode-id=" + episode_id + "]");

        old_up.removeClass("up");
        old_selected.removeClass("selected").addClass("up");
        setTimeout(function() {
            if (!old_selected.is(".selected"))
                old_selected.removeClass("up");
        }, 1000);

        target_carton.addClass("selected");
    }

    function selectEpisode(episode) {
        if (episode.is(":not(.selected)")) {
            episodes.removeClass("selected");
            episode.addClass("selected");

            showCartonForEpisodeId(episode.data("episode-id"));
        }
    }


    episodes.not(".in-the-past").repeat().each($).then(function() {
        selectEpisode(this);
    }).wait(12000);

    episodes.on('click', function(event){
        episodes.unwait().then(function() {
            selectEpisode($(event.delegateTarget));
        });
    });
});