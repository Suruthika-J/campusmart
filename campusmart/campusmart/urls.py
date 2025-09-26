from django import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect 
from django.views import View
from django.contrib.auth import views as auth_views # ← Add this line
import market.views
from market import views

urlpatterns = [
    path('', lambda request: redirect('/market/add/')),  # ← Redirect root to item form
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('market/', include('market.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/signup/', market.views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', lambda request: redirect('login')),  # root goes to login
    path('market/', include('market.urls')),
    path('market/', include(('market.urls', 'market'), namespace='market')),
    path('market/buy_item/<int:item_id>/', views.buy_item, name='buy_item'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)