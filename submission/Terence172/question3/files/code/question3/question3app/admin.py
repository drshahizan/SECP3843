from django.contrib import admin
from .models import CustomUser, UserProfile

admin.site.register(CustomUser)
admin.site.register(UserProfile)
