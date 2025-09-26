from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

from .models import Item, Transaction, ChatMessage
from .forms import ItemForm, SearchForm, ChatForm, TransactionForm


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('search_items')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def dashboard(request):
    user = request.user

    # Fetch items (optional filter: only items by this user)
    items = Item.objects.all()  # or .filter(seller=user) if needed

    # Latest 5 messages
    messages_list = ChatMessage.objects.filter(receiver=user).order_by('-timestamp')[:5]  # correct field

    # Latest 5 transactions
    transactions = Transaction.objects.filter(buyer=user).order_by('-created_at')[:5]  # correct field

    return render(request, 'market/dashboard.html', {
        'items': items,
        'messages': messages_list,
        'transactions': transactions,
    })

@login_required
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.seller = request.user
            item.save()
            return redirect('search_items')
    else:
        form = ItemForm()
    return render(request, 'market/add_item.html', {'form': form})


def item_success(request):
    return render(request, 'market/item_success.html')


def search_items(request):
    form = SearchForm(request.GET or None)
    items = Item.objects.all()
    if form.is_valid():
        query = form.cleaned_data.get('query')
        category = form.cleaned_data.get('category')
        if query:
            items = items.filter(title__icontains=query)
        if category:
            items = items.filter(category=category)
    return render(request, 'market/search_items.html', {'form': form, 'items': items})



