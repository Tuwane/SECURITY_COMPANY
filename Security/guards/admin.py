from django.contrib import admin
from . models import Guard, Deployment, GuardContract
# Register your models here.



admin.site.register(Guard)
admin.site.register(Deployment)
admin.site.register(GuardContract)
