from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from deck.models import Show, Carton, Episode, Download, Category
from models import UserProfile

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

class CartonInline(admin.StackedInline):
    model = Carton
    fk_name = 'episode'
    extra = 0
    exclude = ('standalone',)

class CustomEpisodeAdmin(admin.ModelAdmin):
    inlines = [DownloadInline, CartonInline]
    list_filter = ('show__name', 'termined')
    ordering = ('-time', )
    date_hierarchy = 'time'
    list_display = ('__unicode__', 'summary', 'time')

class CustomCartonAdmin(admin.ModelAdmin):
    list_filter = ('episode__show__name', 'visible')
    ordering = ('-published_at', )
    date_hierarchy = 'published_at'
    list_display = ('__unicode__', 'grand_titre', 'published_at', 'visible')

admin.site.register(Show)
admin.site.register(Carton, CustomCartonAdmin)
admin.site.register(Episode, CustomEpisodeAdmin)
admin.site.register(Category)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)