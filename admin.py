from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
import modelclone
from deck.models import Show, Episode, Download, Category, LivePage, Producer
from models import UserProfile


class DefaultFilterMixIn(admin.ModelAdmin):
    def changelist_view(self, request, *args, **kwargs):
        from django.http import HttpResponseRedirect
        if self.default_filters:
            try:
                test = request.META['HTTP_REFERER'].split(request.META['PATH_INFO'])
                if test and test[-1] and not test[-1].startswith('?'):
                    url = reverse('admin:%s_%s_changelist' % (self.opts.app_label, self.opts.module_name))
                    filters = []
                    for filter in self.default_filters:
                        key = filter.split('=')[0]
                        if not request.GET.has_key(key):
                            filters.append(filter)
                    if filters:
                        return HttpResponseRedirect("%s?%s" % (url, "&".join(filters)))
            except Exception:
                pass
        return super(DefaultFilterMixIn, self).changelist_view(request, *args, **kwargs)


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    fk_name = 'user'
    min_num = 1
    max_num = 1


class CustomUserAdmin(UserAdmin):
    inlines = [UserProfileInline, ]
    #list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')


class DownloadInline(admin.TabularInline):
    model = Download
    fk_name = 'episode'
    extra = 0


class CustomEpisodeAdmin(modelclone.ClonableModelAdmin):
    js = ('js/admin.js', )

    inlines = [DownloadInline, ]
    list_filter = ('show__category', 'show__name')
    ordering = ('-time', )
    date_hierarchy = 'time'
    list_display = ('__unicode__', 'summary', 'time')


class CustomShowAdmin(DefaultFilterMixIn):
    default_filters = ('archived__exact=0',)
    ordering = ('short', )
    list_filter = ('category', 'archived')
    list_display = ('short', 'name', 'category', 'average_duration', 'archived')


class CustomLivePageAdmin(DefaultFilterMixIn):
    default_filters = ('show__archived__exact=0', )
    ordering = ('show__name', )
    list_filter = ('show__archived', )
    list_display = ('__unicode__', )


admin.site.register(Show, CustomShowAdmin)
admin.site.register(Episode, CustomEpisodeAdmin)
admin.site.register(Category)
admin.site.register(Producer)
admin.site.register(LivePage, CustomLivePageAdmin)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)