from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import FormView, CreateView
from .forms import LoginForm, RegisterForm



def login_page(request):
    #Creates the login form 
    form = LoginForm(request.POST or None)
    context = {
        "form":  form
    }
    #Checks if form is valid
    if form.is_valid():
        #Gets the data from the form
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        #Checks if user details are correct
        user = authenticate(request, email=email, password=password)
        #If user exists
        if user is not None:
            #Logs in user
            login(request, user)
            #Redirects user to /
            return redirect('/')
        else:
            print('Error,', form.errors)
    #Return the login webpage to the user
    return render(request, "login.html", context)

def logout_page(request):
    #Logs the user out
    logout(request)
    #Returns the user to the logout page
    return redirect('Core:index')

class RegisterView(CreateView):
    #Creates a registration form
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = '/'

def AccountView(request):
    user = request.user
    context = {'user':user}
    return render(request, 'account.html', context)
