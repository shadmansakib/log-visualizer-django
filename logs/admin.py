from django.contrib import admin

from logs.models import Log, Category

admin.site.register(Category)
admin.site.register(Log)
