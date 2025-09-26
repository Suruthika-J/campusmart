from django.contrib import admin
from .models import Item, ChatMessage, Transaction

# Register Item
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'seller', 'posted_at')

