from django.urls import path
from . import views
from .views import TrailDetailView, TrailListView

urlpatterns = [

      # Homepage
 
    path('', views.TrailListView.as_view(), name='home'),
    # ... your other paths like trail_detail ...

    path('trail/<slug:slug>/', TrailDetailView.as_view(), name='trail_detail'),    

    path('about/', views.about, name='about'),

    path('trailmaps/', views.trail_maps_view, name='trail_maps_view'),


  
]

