
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from follower.models import Fallower
from .forms import RegistrationForm

# Create your views here.
def register(request):
    form=RegistrationForm()
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data['name']
            last_name=form.cleaned_data['surname']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            phone_number=form.cleaned_data['phone_number']

            user =Fallower.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password )
            user.phone_number=phone_number
            user.save()
    else:        
        form=RegistrationForm()

    context={
        'form':form
    }
    return (request,'registration/signup.html', context )



class SignUpView(generic.CreateView):
    form_class=UserCreationForm
    success_url= reverse_lazy('blog:home_page')
    template_name='registration/signup.html'


class LoginView(View):
    def get(self, request):
        return render(request, 'registration/login.html')


    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        check = User.objects.filter(username=username)
        print(check)
        if check:
            user= User.objects.get(username=username)
            user = authenticate(request,username=username,password=password)
        
            if user:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, " Mufaqatli o`tdingiz" )
                return redirect ('blog:home_page')
                
            else:
                messages.add_message(request, messages.WARNING, "PAROL NOTOGRI")
        else:
            messages.add_message(request, messages.WARNING, "BUNDAY USER MAVJUD EMAS!")
        return redirect ('follower:login')




def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password )
        return render (request, 'index.html ')

        if user is not None:
            login(request, user)
            return redirect('index')

        else:
            messages.success(request,('error') )
            return redirect ('registration/login.html')
    else:
        return redirect (request, 'registration/login.html')