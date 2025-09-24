from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Item
from .forms import ItemForm
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def dashboard(request):
    user = request.user
    items = Item.objects.all()  # or .filter(seller=user) if needed
    return render(request, 'market/dashboard.html', {
        'items': items,
    })

@login_required
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.seller = request.user
            item.save()
            return redirect('dashboard')
    else:
        form = ItemForm()
    return render(request, 'market/add_item.html', {'form': form})
def item_success(request):
    return render(request, 'market/item_success.html')
