from django.contrib import admin

from .models import PersonalInformation, Skills, Educations
from django.contrib.admin.models import LogEntry

LogEntry.objects.all().delete()

# Register your models here.
admin.site.register(PersonalInformation)
admin.site.register(Skills)
admin.site.register(Educations)
