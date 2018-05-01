from django.contrib import admin

# Register your models here.
from .models import Posts

admin.site.register(Posts)
class Meta:
    verbose_name_plural = "Posts"
