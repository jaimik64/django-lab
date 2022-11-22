from django.shortcuts import render,redirect
from .forms import signupForm,loginForm,extraDataForm
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from socialMediaApp import settings
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from .tokens import generate_token
from django.contrib.auth import login
from .models import UserExtraData
import datetime

@csrf_exempt 
def mainPage(req):
    return render(req,'mainPage.html')

@csrf_exempt
def signup(request):
  if request.method == 'POST':
      form = signupForm(request.POST)
      if form.is_valid():
        username=request.POST['username']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        emailId=request.POST['emailId']

        if User.objects.filter(username=username):
            messages.error(
                request, "Username already exist! Please try some other username.")
            return render(request,"signup.html",{"form":form})

        if User.objects.filter(email=emailId).exists():
            messages.error(request, "Email Already Registered!!")
            return render(request,"signup.html",{"form":form})

        if len(username) > 20:
            messages.error(request, "Username must be under 20 charcters!!")
            return render(request,"signup.html",{"form":form})

        if password != confirm_password:
            messages.error(request, "Passwords didn't matched!!")
            return render(request,"signup.html",{"form":form})

        if not username.isalnum():  # New_User1 x
            messages.error(request, "Username must be Alpha-Numeric!!")
            return render(request,"signup.html",{"form":form})

        myuser = User.objects.create_user(username, emailId, password)
        myuser.is_active = False
        myuser.save()

        messages.success(
            request, "Your accunt is successfully created!!! Please check your email to confirm your email address in order to activate your account.")

        subject = "Welcome to the Social Media!!"
        message = "Hello " + myuser.username + "!! \n Welcome to Social Media!! \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address. \n\nhappy Trading\n Stock Triainer Developer Team"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        # Email Address Confirmation Email
        current_site = get_current_site(request)
        email_subject = "Confirm your Email for Social Media!!"
        message2 = render_to_string('email_confirmation.html', {

            'name': myuser.username,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })
        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email],
        )
        email.fail_silently = True
        email.send()

        return redirect('login')
  else:
      form = signupForm()

  return render(request, 'signup.html', {'form': form})

def extraData(request):
  form=extraDataForm()
  if request.method == 'POST':
      form = extraDataForm(request.POST)
      if form.is_valid():
        birthDate=request.POST['birthDate']
        mobileNo=request.POST['mobileNo']
        gender=request.POST['gender']
        city=request.POST['city']
        pincode=request.POST['pincode']
        state=request.POST['state']

        # UserExtraData(form)
        data = form.save(commit=False)
        data.user=request.user
        data.birthDate = birthDate
        data.mobileNo = mobileNo
        data.gender = gender
        data.city = city
        data.pincode = pincode
        data.state = state

        today = datetime.date.today()
        st=birthDate.split("-")
        age= today.year - int(st[0]) - ((today.month, today.day) < (int(st[1]), int(st[2])))
        data.age=age
        print(age)
        data.save()

        return redirect('login')
  else:
      form = extraDataForm()

  return render(request, 'extraData.html', {'form': form})


def activate(request,uidb64,token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        login(request,myuser)
        messages.success(request, "Your Account has been activated!!")
        return redirect('extraData')
    else:
        return render(request,'activation_failed.html')
