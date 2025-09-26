from django import forms
from .models import Item, CATEGORY_CHOICES
from django import forms
from .models import ChatMessage
from .models import Transaction


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'description', 'category', 'price', 'image']

class SearchForm(forms.Form):
    query = forms.CharField(required=False, label='Search')
    category = forms.ChoiceField(choices=[('', 'All')] + CATEGORY_CHOICES, required=False)

