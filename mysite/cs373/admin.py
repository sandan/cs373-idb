from django.contrib import admin
from cs373.models import *
# Register your models here.

class StageMediaInline(admin.StackedInline):
    model = StageMedia
    extra = 0

class StageAdmin(admin.ModelAdmin):
    inlines = [StageMediaInline]

class SponsorMediaInline(admin.StackedInline):
    model = SponsorMedia
    extra = 0

class SponsorAdmin(admin.ModelAdmin):
    inlines = [SponsorMediaInline]

class ArtistMediaInline(admin.StackedInline):
    model = ArtistMedia
    extra = 0

class ArtistAdmin(admin.ModelAdmin):
    inlines = [ArtistMediaInline]


admin.site.register(Stage, StageAdmin)
admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(Artist, ArtistAdmin)
