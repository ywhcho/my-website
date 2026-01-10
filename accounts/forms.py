from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        required=True,
        help_text='필수 입력 사항입니다.',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': '이메일'})
    )
    username = forms.CharField(
        max_length=150,
        required=True,
        help_text='150자 이하의 문자, 숫자 및 @/./+/-/_ 만 사용 가능합니다.',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '사용자명'})
    )
    password1 = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '비밀번호'})
    )
    password2 = forms.CharField(
        label='비밀번호 확인',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '비밀번호 확인'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
