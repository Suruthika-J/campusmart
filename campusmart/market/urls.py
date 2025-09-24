from django.urls import path
from django.contrib.auth import views as auth_views  
from . import views

urlpatterns = [
    # Item management
    path('add/', views.add_item, name='add_item'),
    path('success/', views.item_success, name='item_success'),

    # Auth
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', views.signup, name='signup'),

    # Dashboard & Home
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
