from django.contrib import admin
from .models import Profile,OfferedSkill,RequestedSkill,Requests

# Register your models here.
admin.site.register(Profile)
admin.site.register(OfferedSkill)
admin.site.register(RequestedSkill)
admin.site.register(Requests)