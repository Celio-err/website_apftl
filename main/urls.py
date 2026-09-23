from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('rejistu/', views.register_view, name='rejistu'),
    path('perfil/', views.profile_view, name='perfil'),
]