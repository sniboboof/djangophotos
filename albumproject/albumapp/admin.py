from django.contrib import admin
from albumapp import models

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Tag)
admin.site.register(models.Photo)
admin.site.register(models.Album)
