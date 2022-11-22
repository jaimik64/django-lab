from datetime import datetime
from django import forms
from django.forms import fields
from django.forms.widgets import EmailInput
from .models import Login,UserExtraData

class loginForm(forms.ModelForm):
  username = forms.CharField()
  password = forms.CharField(widget=forms.PasswordInput)
  
  class Meta:
    model = Login
    fields=['username','password']

class signupForm(forms.ModelForm):
  username = forms.CharField()
  emailId = forms.CharField(widget=EmailInput)
  password = forms.CharField(widget=forms.PasswordInput)
  confirm_password = forms.CharField(widget=forms.PasswordInput)
  class Meta:
    model = Login
    fields=['username','emailId','password','confirm_password']



class extraDataForm(forms.ModelForm):
  birthDate = forms.DateField(required=False,input_formats=["%Y-%m-%d"],widget=forms.DateInput(attrs={'class': 'form-control'}))
  mobileNo = forms.CharField(label="Mobile No.", widget=forms.NumberInput)
  gender = forms.CharField(label="Gender",widget=forms.RadioSelect(choices=[("male","Male"),("female","Female")]))
  city=forms.CharField(label="City", required=False)
  pincode=forms.CharField(label="Pincode",required=False)
  state=forms.CharField(label="State",required=False)
  class Meta:
    model = UserExtraData
    fields=['birthDate','mobileNo','gender','city','pincode','state']