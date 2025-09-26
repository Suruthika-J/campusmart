from django.urls import path
from django.contrib.auth import views as auth_views   # ✅ this was missing
from . import views

urlpatterns = [
    path('add/', views.add_item, name='add_item'),
    path('success/', views.item_success, name='item_success'),
    path('search/', views.search_items, name='search_items'),
    path('chat/send/', views.send_message, name='send_message'),
    path('chat/inbox/', views.inbox, name='inbox'),
    path('transaction/create/<int:item_id>/', views.create_transaction, name='create_transaction'),
    path('transaction/list/', views.transaction_list, name='transaction_list'),
    path('add/', views.add_item, name='add_item'),
    # market/urls.py
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('', views.home, name='home'),  # homepage after login
    path('signup/', views.signup, name='signup'),
    path('pay_transaction/<int:txn_id>/', views.pay_transaction, name='pay_transaction'),  # new payment URL
    path('search/', views.search_items, name='search_items'),
    path('buy/<int:item_id>/', views.buy_item, name='buy_item'),  # <- this is needed
    path('transaction_list/', views.transaction_list, name='transaction_list'),

]