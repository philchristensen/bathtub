from django.contrib import admin

from bathtub.common.models import Show

class ShowAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
admin.site.register(Show, ShowAdmin)
