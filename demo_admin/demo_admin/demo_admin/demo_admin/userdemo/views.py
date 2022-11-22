from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import UserForm, ProfileForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm #add this



# Create your views here.
def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.hobby = 'Coding, Chess, Guitar'
    user.save()

def profile(request):
    if request.method == 'POST':
        #print(request.username)
        u_form = UserForm(request.POST, instance=request.user)
        #print(request.user)
        p_form = ProfileForm(request.POST, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            u_form = UserForm(instance=request.user)
            p_form = ProfileForm(instance=request.user.profile)
            #u_form=UserForm()
            #p_form=ProfileForm()
            context = {
                    'u_form': u_form,
                    'p_form': p_form
                }
            return render(request, 'profile.html',context)
    else:
        u_form = UserForm(instance=request.user)
        p_form = ProfileForm(instance=request.user.profile)
        #u_form=UserForm()
        #p_form=ProfileForm()
        context = {
                    'u_form': u_form,
                    'p_form': p_form
                }
    return render(request, 'profile.html', context)

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                u_form = UserForm(instance=request.user)
                p_form = ProfileForm(instance=request.user.profile)
                #u_form=UserForm()
                 #p_form=ProfileForm()
                context = {
                    'u_form': u_form,
                    'p_form': p_form
                }
                return render(request, 'profile.html',context)
                #return redirect("/")
                #return render(request, 'profile.html') 
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})

