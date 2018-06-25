from django import forms
from .models import Profile



class PostCreateForm(forms.Form):
    title = forms.CharField(label='title', max_length=100, widget=forms.TextInput(attrs={'size': 40}))
    content = forms.CharField(label='content', widget=forms.Textarea(attrs={'rows': 8,'cols': 120}))

class CommentCreateForm(forms.Form):
    content = forms.CharField(label='content', widget=forms.Textarea(attrs={'rows': 8,'cols': 120}))


class RegisterForm(forms.Form):
    username = forms.CharField(label='username', max_length=20)
    password = forms.CharField(label = 'password', max_length=20, widget=forms.PasswordInput())
    email = forms.EmailField(label = 'email')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput())

class ProfileForm(forms.Form):
    M = 'Male'
    F = 'Female'
    U = 'Unknown'
    sex_choice = (
        (M, 'Male'),
        (F, 'Female'),
        (U, 'Unknown')
    )
    sex = forms.MultipleChoiceField(choices=sex_choice)
    age = forms.IntegerField(label='age')
    introduction = forms.CharField(max_length=3000, widget=forms.Textarea(attrs={'rows': 8,'cols': 120}))

