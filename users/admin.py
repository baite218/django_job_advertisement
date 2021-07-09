from django.contrib import admin
from .models import Profile, Professions, ProfileResume, Subscriber

class SubscriberInline(admin.TabularInline):
    model = Subscriber
    extra = 0
    fk_name = 'follower'

class ProfileAdmin(admin.ModelAdmin):
    inlines = [SubscriberInline]

admin.site.register(Profile, ProfileAdmin)
admin.site.register(ProfileResume)
admin.site.register(Professions)
admin.site.register(Subscriber)
