from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import FoodItem, Restaurant
from django.contrib.auth.decorators import login_required
from .forms import FoodItemForm, SignUpForm

# ----------------------------
# Restaurant signup
# ----------------------------
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.save()

            # Create linked Restaurant
            restaurant_name = form.cleaned_data.get('restaurant_name') or user.username
            Restaurant.objects.create(
                user=user,
                name=restaurant_name,
                address='',
                phone_number='',
                email=user.email
            )

            # Log in the user
            login(request, user)
            messages.success(request, "Account created successfully")
            return redirect('dashboard')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = SignUpForm()

    return render(request, 'restaurants/signup.html', {'form': form})

# ----------------------------
# Restaurant login
# ----------------------------
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # safer
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # or wherever
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, 'restaurants/login.html')

# ----------------------------
# Restaurant logout
# ----------------------------
def logout_view(request):
    logout(request)
    return redirect('login')

# ----------------------------
# Restaurant dashboard
# ----------------------------
@login_required
def dashboard_view(request):
    try:
        restaurant = Restaurant.objects.get(user=request.user)
    except Restaurant.DoesNotExist:
        messages.error(request, "No restaurant linked to this user.")
        return redirect('signup')

    # Handle form submission
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            food_item = form.save(commit=False)
            food_item.restaurant = restaurant
            food_item.save()
            messages.success(request, "Food item added successfully.")
            return redirect('dashboard')
    else:
        form = FoodItemForm()

    menu_items = restaurant.menu_items.all()  # related_name='menu_items'
    return render(request, 'restaurants/dashboard.html', {'menu_items': menu_items, 'form': form})

def edit_food_item(request, pk):
    food = get_object_or_404(FoodItem, pk=pk)
    if request.method == 'POST':
        form = FoodItemForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = FoodItemForm(instance=food)
    
    return render(request, 'restaurants/edit_food_item.html', {'form': form})

def delete_food_item(request, pk):
    food = get_object_or_404(FoodItem, pk=pk)
    # Optional: only allow the owner restaurant to delete
    if food.restaurant == request.user.restaurant:
        food.delete()
    return redirect('dashboard')