from django.contrib import admin

from apis.products import models



admin.site.register(models.Category)
admin.site.register(models.Sub_Category)
admin.site.register(models.Product)
