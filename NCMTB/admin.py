from django.contrib import admin

from .models import TrailArticle, Comment

# Register your models here.
admin.site.register(TrailArticle)
admin.site.register(Comment)