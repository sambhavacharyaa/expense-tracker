from . import views
from django.urls import path, include


urlpatterns = [
    
    path('', views.index, name='index' ),
    path('dashboard/', views.dashboard, name='dashboard' ),
    path('charts/', views.charts, name='charts' ),
    path('report/', views.reports, name='report' ),
] 