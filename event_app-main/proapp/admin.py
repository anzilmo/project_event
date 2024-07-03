from django.contrib import admin
from .models import Event,Booking
from django.utils.safestring import mark_safe


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc', 'img_preview')
    search_fields = ('name', 'desc')
    list_filter = ('name',)

    def img_preview(self, obj):
        return obj.img and mark_safe(f'<img src="{obj.img.url}" width="50" height="50" />') # type: ignore
    img_preview.short_description = 'Image Preview'
    img_preview.allow_tags = True

admin.site.register(Event, EventAdmin)
admin.site.register(Booking)