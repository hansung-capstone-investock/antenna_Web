from django.contrib import admin
from .models import dcData, fmkorData, companyData, MainNews

admin.site.register(dcData)
admin.site.register(fmkorData)
admin.site.register(companyData)
admin.site.register(MainNews,MainNewsAdmin)

class MainNewsAdmin(admin.ModelAdmin):
    list_display = ('title','summery','publishDay','link')
    
