if (!$) {
    $ = django.jQuery;
}

function overrideTimeOptions() {
    var TIME_CHOICES = {
      '16:00': '16,00,0',
      '18:00': '18,00,0',
      '20:30': '20,30,0',
      '21:00': '21,00,0',
      '21:57': '21,57,0',
      '22:00': '22,00,0',
      '23:00': '23,00,0'
    };

    $("ul.timelist").each(function(){
        var entries = $(this).children("li");

        var baseEntry = entries.first();
        var baseHref = baseEntry.find("a").attr("href");

        entries.remove();

        $.each(TIME_CHOICES, function(label, value) {
            var newEntryHref = baseHref.replace(/Date\([^\)]*\)/g, "Date(1970,1,1," + value + ",0)");
            var newEntry = '<li><a href="'+ newEntryHref +'">' + label + '</a></li>';
            $(this).append(newEntry);
        }.bind(this));
    });
}
function computeTimeFieldMoment(element) {
    var dateFieldVal = $(element).find("input.vDateField").val(),
        timeFieldVal = $(element).find("input.vTimeField").val();

    if (dateFieldVal && timeFieldVal) {
        return moment([dateFieldVal, timeFieldVal].join("-"), "DD/MM/YYYY-HH:mm:SS")
    } else {
        return false;
    }
}
function setTimeFieldMoment(element, moment) {
    var dateField = $(element).find("input.vDateField"),
        timeField = $(element).find("input.vTimeField");

    dateField.val(moment.format("DD/MM/YYYY"));
    timeField.val(moment.format("HH:mm:SS"));
}

var deckAllShows = null;
var currentShowDuration = null;

function fetchAverageDuration() {
    var idShow = $("#id_show").val();

    if (!deckAllShows) {
        return $.getJSON("http://localhost:8000/feeds/shows.json", function (data) {
            if (data) {
                deckAllShows = data;
                fetchAverageDuration();
            }
        });
    } else {
        if (deckAllShows[idShow]) {
            currentShowDuration = deckAllShows[idShow].average_duration;

            var momentDuration = moment.duration({ minutes: currentShowDuration }),
                hoursLabel = currentShowDuration > 119 ? "heures" : "heure",
                minutesLabel = currentShowDuration % 60 > 1 ? "minutes" : "minute",
                humanized = [currentShowDuration, "minutes"].join(" ");

            if (currentShowDuration > 59) {
                if (currentShowDuration % 60) {
                    humanized = [Math.floor(momentDuration.asHours()), hoursLabel, "et", momentDuration.minutes(), minutesLabel].join(" ");
                } else {
                    humanized = [Math.floor(momentDuration.asHours()), hoursLabel].join(" ");
                }
            }

            $(".field-end_time .datetime .autofillnow").show();
            $(".field-end_time .datetime .autofillnow em").text(["Ajouter", humanized].join(" ")).css("font-style", "normal");
        } else {
            $(".field-end_time .datetime .autofillnow").hide();
        }
    }
}

$(document).ready(function() {
    setTimeout(function(){overrideTimeOptions()},500);

    $(".field-end_time .datetime").before('' +
        '<p class="datetime autofillwrap" style="font-weight: normal; margin-bottom: 5px;">' +
            '<a href="#autofill" class="autofillnow">' +
            '<img alt="Horloge" src="/static/admin/img/icon_clock.gif"> <em>Calculer automatiquement</em> à partir de l\'heure de début</a>' +
        '</p>'
    );

    fetchAverageDuration();

    $("#id_show").change(function() {
        fetchAverageDuration();
    });

    $(".field-end_time .autofillnow").click(function(event) {
        var timeMoment = computeTimeFieldMoment(".field-time");

        if (currentShowDuration && timeMoment) {
            setTimeFieldMoment(".field-end_time", timeMoment.add('minutes', currentShowDuration));
        }
    });
});