from django.contrib import admin

from .models import TrailArticle, Comment, Blog

# Register your models here.
admin.site.register(TrailArticle)
admin.site.register(Blog)
admin.site.register(Comment)