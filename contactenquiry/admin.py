from django.contrib import admin
from contactenquiry.models import ContactEnquiry

# Register your models here.
class enquiryAdmin(admin.ModelAdmin):
    list_display=('name','email','phone','msg')

admin.site.register(ContactEnquiry,enquiryAdmin)