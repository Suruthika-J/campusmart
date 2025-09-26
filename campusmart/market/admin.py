from django.contrib import admin
from .models import Item, ChatMessage, Transaction

# Register Item
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'seller', 'posted_at')

# Register ChatMessage
@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'message')

# Register Transaction
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('item', 'buyer', 'seller', 'created_at', 'payment_status')  # use created_at instead of timestamp
    list_filter = ('payment_status', 'created_at')  # must be tuple or list
    search_fields = ('item__title', 'buyer__username', 'seller__username')

# ❌ Remove this duplicate registration
# admin.site.register(Transaction, TransactionAdmin)
