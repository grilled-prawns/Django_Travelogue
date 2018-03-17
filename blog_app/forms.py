from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):

    text = forms.CharField(label='Text', max_length=2000,
                           widget=forms.Textarea(attrs={'rows': '20', 'cols': '135'}))

    class Meta:
        model = Post
        fields = ('title', 'text', 'post_picture')

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )