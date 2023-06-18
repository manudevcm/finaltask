from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# from .models import Department


# Create your views here.
def index(request):
    # department = Department.objects.all()
    # context = {'department': department}
    return render(request, 'index.html')


def edit(request):
    # department = Department.objects.all()
    # context = {'department': department}
    return render(request, 'edit.html')


def login_request(request):
    # department = Department.objects.all()
    # context = {'department': department}

    user = auth.authenticate()

    if user is not None:
        messages.info(request, "Order Confirmed")
        return redirect('/')

    return render(request, 'login_request.html')


def login(request):
    # department = Department.objects.all()
    # context = {'department': department}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')

    return render(request, "login.html")


def register(request):
    # department = Department.objects.all()
    # context = {'department': department}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.info(request, "user created")
                return redirect('login')
    return render(request, "register.html")


def message(request):
    return render(request, "message.html")
