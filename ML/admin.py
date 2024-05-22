from django.contrib import admin

# Register your models here.
import ML.models as models

admin.site.register(models.Topic)
admin.site.register(models.Entry)