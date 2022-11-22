from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth import login, logout,authenticate
from django.contrib import messages
from django.views.generic import CreateView
from .forms import CustomerSignUpForm, EmployeeSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User
# Create your views here.

def register(request):
    return render(request, 'register.html')

def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request,'index.html')

class customer_register(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'customer_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return render(self.request,'index.html')

class employee_register(CreateView):
    model = User
    form_class = EmployeeSignUpForm
    template_name = 'employee_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return render(self.request,'index.html')


def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return render(request,'index.html')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'login.html',
    context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    # form = AuthenticationForm()
    return render(request,'home.html')
