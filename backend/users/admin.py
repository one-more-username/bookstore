from django.contrib import admin

from .models import Profile

# Register your models here.

# inline for render profile

admin.site.register(Profile)
