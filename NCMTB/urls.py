from django.urls import path
from . import views
from .views import TrailDetailView, TrailListView

urlpatterns = [

      # Homepage
 
    path('', views.TrailListView.as_view(), name='home'),
    # ... your other paths like trail_detail ...

    path('trail/<slug:slug>/', TrailDetailView.as_view(), name='trail_detail'),

    path('beginnertrails/', views.beginner_trails, name='beginner'),

    path('intermediatetrails/', views.advanced_trails, name='advanced'),
    
    path('advancedtrails/', views.intermediate_trails, name='intermediate'),

    path('experttrails/', views.expert_trails, name='expert'),

    path('reccs/', views.reccs, name='reccs'),

    path('browse/', views.browse, name='browse'),
    
    path('interest/', views.interest, name='interest'),

    path('about/', views.about, name='about'),


  
]

