from django import forms
from .models import Item, CATEGORY_CHOICES


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'description', 'category', 'price', 'image']
