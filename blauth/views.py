from django.shortcuts import render, redirect, reverse
from django.http.response import JsonResponse
import string
import random
from django.core.mail import send_mail
from .models import CaptchaModel
from django.views.decorators.http import require_http_methods
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout

# Create your views here.
@require_http_methods(["GET", "POST"])
def bllogin(request):
    if request.method == "GET":
        return render(request, 'html/login.html')
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            remember = form.cleaned_data.get('remember')
            user = User.objects.filter(email=email).first()
            if user and user.check_password(password):
                login(request, user)

                if not remember:
                    request.session.set_expiry(0)
                return redirect('/')
            else:
                print('邮箱或密码错误')
                form.add_error('email', '邮箱或密码错误')
                return render(request, 'html/login.html', {'form': form})


@require_http_methods(['POST', 'GET'])
def register(request):
    if request.method == 'GET':
        return render(request, 'html/register.html')
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            username = form.cleaned_data.get('username')
            user = User.objects.create_user(email=email, username=username, password=password)
            return redirect(reverse('blauth:bllogin'))
        else:
            print(form.errors)
            return redirect(reverse('blauth:register'))
            # return render(request, 'html/register.html', {'form': form})


def send_email_captcha(request):

    email = request.GET.get('email')
    if not email:
        return JsonResponse({"code": 400, "message": '必须传递邮箱!'})
    captcha = "".join(random.sample(string.digits, 4))
    CaptchaModel.objects.update_or_create(email=email, defaults={'captcha': captcha})
    send_mail("注册验证码", message=f"您的注册验证码是：{captcha}", recipient_list=[email], from_email=None, fail_silently=False)
    return JsonResponse({"code": 200, "message": '发送成功!'})


def blog_logout(request):
    logout(request)
    return redirect('/')