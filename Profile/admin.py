from django.contrib import admin
from Profile.models import *
from nested_admin import NestedTabularInline


class HistoriesInline(NestedTabularInline):
    model = Histories
    extra = 1

class ProfileAdmin(admin.ModelAdmin):
    inlines = [HistoriesInline]

admin.site.register(Profile, ProfileAdmin)
