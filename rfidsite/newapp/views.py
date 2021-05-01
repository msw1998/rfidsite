from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from .forms import NewUserForm
from django.contrib import messages

def index(request,  *args, **kwargs):
    return render(request=request, 
                  template_name="newapp/index.html",)

        
    print("Hello World")        
 
def login_request(request):
    if request.method=="POST":
        form = AuthenticationForm(request = request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return render(request = request,
                             template_name = "newapp/index.html")
                
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
  
    form = AuthenticationForm()
    return render(request = request,
                  template_name = "newapp/loginpage.html",
                  context={"form":form})



def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New Account Created: {username}")
            login(request, user)
            return render(request=request, 
                          template_name="newapp/loginpage.html",)
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request = request,
                          template_name = "newapp/register.html",
                          context={"form":form})
    form = NewUserForm
    return render(request = request,
                  template_name = "newapp/register.html",
                  context={"form":form})

