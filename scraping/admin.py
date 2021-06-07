from django.contrib import admin
from .models import dcData, companyData, MainNews


# class MainNewsAdmin(admin.ModelAdmin):
#     list_display = ('title','summary','publishDay','link')
    

admin.site.register(dcData)
admin.site.register(companyData)
# admin.site.register(MainNews,MainNewsAdmin)
admin.site.register(MainNews)