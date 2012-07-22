from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from deck.models import Show, Carton, Episode, Download
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

class CustomEpisodeAdmin(admin.ModelAdmin):
    inlines = [DownloadInline,]

admin.site.register(Show)
admin.site.register(Carton)
admin.site.register(Episode, CustomEpisodeAdmin)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)