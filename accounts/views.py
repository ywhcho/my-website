from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import SignUpForm


def signup(request):
    """회원가입 뷰"""
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # 회원가입 후 자동 로그인
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'{username}님, 회원가입을 환영합니다!')
            return redirect('index')
        else:
            messages.error(request, '회원가입에 실패했습니다. 입력 내용을 확인해주세요.')
    else:
        form = SignUpForm()
    
    return render(request, 'accounts/signup.html', {'form': form})


def user_login(request):
    """로그인 뷰"""
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'{username}님, 환영합니다!')
                return redirect('index')
            else:
                messages.error(request, '사용자명 또는 비밀번호가 올바르지 않습니다.')
        else:
            messages.error(request, '사용자명 또는 비밀번호가 올바르지 않습니다.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {'form': form})


def user_logout(request):
    """로그아웃 뷰"""
    logout(request)
    messages.info(request, '로그아웃되었습니다.')
    return redirect('index')

