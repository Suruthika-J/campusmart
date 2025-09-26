from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

from .models import Item, Transaction, ChatMessage
from .forms import ItemForm, SearchForm, ChatForm, TransactionForm

# -----------------------------
# User Signup
# -----------------------------
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

# -----------------------------
# Homepage / Dashboard
# -----------------------------
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

# -----------------------------
# Item Management
# -----------------------------
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

# -----------------------------
# Chat System
# -----------------------------
@login_required
def send_message(request):
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            chat = form.save(commit=False)
            chat.sender = request.user
            chat.save()
            return redirect('inbox')
    else:
        form = ChatForm()
    return render(request, 'market/send_message.html', {'form': form})


@login_required
def inbox(request):
    messages_list = ChatMessage.objects.filter(receiver=request.user).order_by('-timestamp')
    return render(request, 'market/inbox.html', {'messages': messages_list})

# -----------------------------
# Transactions / Buying
# -----------------------------
@login_required
def create_transaction(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.buyer = request.user
            transaction.item = item
            transaction.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm(initial={'item': item})
    return render(request, 'market/create_transaction.html', {'form': form, 'item': item})

@login_required
def buy_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    Transaction.objects.create(
        item=item,
        buyer=request.user,
        seller=item.seller,
        payment_status='pending'
    )
    messages.success(request, f"You bought {item.title}. Payment pending to {item.seller.username}.")
    return redirect('market:transaction_list')


@login_required
def transaction_list(request):
    transactions = Transaction.objects.filter(buyer=request.user)
    return render(request, 'market/transaction_list.html', {'transactions': transactions})


@login_required
def pay_transaction(request, txn_id):
    txn = get_object_or_404(Transaction, id=txn_id, buyer=request.user)
    txn.payment_status = 'paid'  # mark as paid
    txn.save()
    messages.success(request, f"Payment completed for {txn.item.title} to {txn.seller.username}.")
    return redirect('transaction_list')
