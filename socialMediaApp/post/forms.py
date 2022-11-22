from django import forms
from .models import Post

class createPostForm(forms.ModelForm):
  post=forms.CharField(label="Post",widget = forms.Textarea)
  image = forms.ImageField(label="Image",required=False)
  title=forms.CharField(label="Title")
  file = forms.FileField(label="File",required=False)
  class Meta:
    model = Post
    fields=['title','post','image','file']