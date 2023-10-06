from django.contrib import admin

# Register your models here.
from .models import PrayerTopic, Prayer
from .models import Video

admin.site.register(PrayerTopic)
admin.site.register(Prayer)
admin.site.register(Video)