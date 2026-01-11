from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': '이메일'
        })
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '사용자명'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': '비밀번호'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': '비밀번호 확인'
        })


class UserProfileForm(forms.ModelForm):
    """사용자 프로필 수정 폼"""
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': '이메일'
        })
    )
    first_name = forms.CharField(
        required=False,
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '이름'
        })
    )
    last_name = forms.CharField(
        required=False,
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '성'
        })
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '사용자명'
            }),
        }
    
    def clean_email(self):
        """이메일 중복 체크"""
        email = self.cleaned_data.get('email')
        if email and User.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            raise forms.ValidationError('이미 사용 중인 이메일입니다.')
        return email
    
    def clean_username(self):
        """사용자명 중복 체크"""
        username = self.cleaned_data.get('username')
        if username and User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
            raise forms.ValidationError('이미 사용 중인 사용자명입니다.')
        return username


class CustomPasswordChangeForm(PasswordChangeForm):
    """비밀번호 변경 폼"""
    old_password = forms.CharField(
        label='현재 비밀번호',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': '현재 비밀번호'
        })
    )
    new_password1 = forms.CharField(
        label='새 비밀번호',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': '새 비밀번호'
        })
    )
    new_password2 = forms.CharField(
        label='새 비밀번호 확인',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': '새 비밀번호 확인'
        })
    )
