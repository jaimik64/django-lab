from django.shortcuts import render
from .forms import UserForm
# Create your views here.
#from django.contrib.auth.forms import UserCreationForm 

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})
