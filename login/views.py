from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# Home Page View
def home(request):
    # Check if the user is authenticated and redirect accordingly
    if request.user.is_authenticated:
        return redirect('login')  # Redirect to login page if logged in
    return render(request, 'home_page.html')

def user_dashboard(request):
    return render(request, 'user_dashboard.html')

# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('user_dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')

    return render(request, 'login.html')

# Logout View
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully!")
    return redirect('home')

# Registration View
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! Please log in.")
            return redirect('login')
        else:
            # If form is not valid, show errors and send back the form
            messages.error(request, "There was an error with your registration. Please try again.")
            return render(request, 'register.html', {'form': form})
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})







