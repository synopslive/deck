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

setTimeout(function(){overrideTimeOptions()},500);