from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin



from .models import TrailArticle, Comment, Blog

# 1. Define the Class FIRST
class MyControlCenterSite(admin.AdminSite):
    site_header = "Project Control Center"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('tech-stack/', self.admin_view(self.tech_stack_view), name="tech_stack"),
        ]
        return custom_urls + urls

    def tech_stack_view(self, request):
        context = {
            **self.each_context(request),
            'title': 'Technology Stack',
        }
        # Point to the specific folder we just created
        return render(request, 'admin/control_center/tech_stack.html', context)

# 2. Create the Instance SECOND
control_center = MyControlCenterSite(name='control_center')

# 3. Register your models LAST using the instance created above
control_center.register(TrailArticle)
control_center.register(Blog)
control_center.register(Comment)

# Register the standard User model to your custom control_center
control_center.register(User, UserAdmin)