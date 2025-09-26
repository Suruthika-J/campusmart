from django.urls import path
from django.contrib.auth import views as auth_views   # ✅ this was missing
from . import views

urlpatterns = [
    path('add/', views.add_item, name='add_item'),
    path('success/', views.item_success, name='item_success'),
    path('search/', views.search_items, name='search_items'),
    path('add/', views.add_item, name='add_item'),
    # market/urls.py
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('', views.home, name='home'),  # homepage after login
    path('signup/', views.signup, name='signup'),
    
    path('search/', views.search_items, name='search_items'),
  

]