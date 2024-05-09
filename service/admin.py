from django.contrib import admin
from service.models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display=('Service_icon','Serice_title','Service_des')

admin.site.register(Service,ServiceAdmin)

#register your model here