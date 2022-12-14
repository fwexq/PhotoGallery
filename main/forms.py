from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.forms import ModelForm, TextInput, Textarea, CharField, FileInput, HiddenInput
from rest_framework.authtoken.models import Token

from main.models import CustomUser, Post
from django.contrib.auth import authenticate
from .models import Comment


class FormValidation:
    def __init__(self, cleaned_data, user=None) -> None:
        self.cleaned_data = cleaned_data
        self.user = user

    def clean_first_name(self):
        self.cleaned_data['first_name'] = self.cleaned_data['first_name'].lower()
        first_name = self.cleaned_data.get('first_name')

        try:
            CustomUser.objects.get(first_name=first_name)
            raise forms.ValidationError(f'first_name "{first_name}" is already in use.')
        except CustomUser.DoesNotExist:
            return self.cleaned_data

    def clean_email(self):
        if not self.cleaned_data.get('email'):
            raise forms.ValidationError('Email address does not exists.')

        self.cleaned_data['email'] = self.cleaned_data['email'].lower()
        email = self.cleaned_data.get('email')

        try:
            CustomUser.objects.get(email=email)
            raise forms.ValidationError(f'Email "{email}" is already in use.')
        except CustomUser.DoesNotExist:
            return self.cleaned_data

    def clean_password(self):
        password = self.cleaned_data.get("password")

        if not password:
            raise forms.ValidationError("Password does not exists")

        return self.cleaned_data

    def clean_confirm_password(self):
        confirm_password = self.cleaned_data.get("confirm_password")
        password = self.cleaned_data.get("password")

        if not confirm_password:
            raise forms.ValidationError("Confirm password does not exists")

        if password != confirm_password:
            raise forms.ValidationError(
                "Password and Confirmed password does not match"
            )

        return self.cleaned_data


class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(label='',
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}))
    email = forms.EmailField(label='',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@mail.ru'}))
    password1 = forms.CharField(label='',
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = None

    class Meta:
        model = CustomUser
        fields = ('first_name', 'email', 'password1')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.email = self.cleaned_data.get('email')
        user.set_password(self.cleaned_data.get('password1'))

        if commit:
            user.save()
        return user


class LoginUserForm(AuthenticationForm):
    # username = None
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True}), required=False)
    email = forms.EmailField(label='',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@mail.ru'}))
    password = forms.CharField(label='',
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email is not None and password:
            self.user_cache = authenticate(
                self.request, email=email, password=password
            )
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

        widgets = {
            'text': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter comment text',
            })
        }


class CreatePostForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreatePostForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = ''
        self.fields['description'].label = ''
        self.fields['photo'].label = ''

    class Meta:
        model = Post
        fields = ('title', 'description', 'photo')

        widgets = {
            "title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title', 'style': 'width:27%',
                                      'style': 'border-radius:10px', 'style': 'width: auto'}),
            "description": Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Enter the description', 'style': 'height:8%',
                       'style': 'border-radius: 10px', 'style': 'width: auto'}),

        }


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = ''
        self.fields['description'].label = ''
        self.fields['photo'].label = ''

    class Meta:
        model = Post
        fields = ('title', 'description', 'photo')

        widgets = {
            "title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title', 'style': 'width:27%'}),
            "description": Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Enter the description', 'style': 'height:8%'}),

        }


class UserUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = ''
        self.fields['last_name'].label = ''
        self.fields['avatar'].label = ''

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'avatar']

        widgets = {
            "first_name": TextInput(attrs={'class': 'form-control', 'placeholder': 'Ivan', 'style': 'width:15%'}),
            "last_name": TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ivanov', 'style': 'width:15%'}),

        }




class RoleAssignment(forms.ModelForm):
    user = forms.MultipleChoiceField(choices=[(item.pk, item) for item in CustomUser.objects.all()])

    class Meta:
        model = CustomUser
        fields = ('user', 'is_superuser', 'is_staff')
