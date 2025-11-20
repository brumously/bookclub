from django.contrib import admin
from bookclub import models

# Register your models here.
#admin.site.register(models.User)
admin.site.register(models.Read)
admin.site.register(models.TBR)
admin.site.register(models.Ask)
admin.site.register(models.Rec)