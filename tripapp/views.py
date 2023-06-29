# Create your views here.
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.template.loader import get_template
from tripapp.forms import ProfileForm, UserLoginForm, AddYourStory, ContactForm, AddYourTrip
from tripapp.models import YourStory, YourTrip


def index(request):
    return render(request, 'index.html', locals())


def about(request):
    return render(request, 'about.html', locals())


def home(request):
    return render(request, 'index.html', locals())


def option(request):
    return render(request, 'option.html', locals())


def javascript(request):
    return render(request, 'javascript.html', locals())


def blog(request):
    blog02 = YourStory.objects.all()
    print(blog02, '********************************************************************************')
    return render(request, 'blog.html', {'blog02': blog02})


def trips(request):
    trip02 = YourTrip.objects.all()
    print(trip02, '********************************************************************************')
    return render(request, 'trips.html', {'trip02': trip02})


def trip_single(request, id):
    print(id, '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    trip01 = get_object_or_404(YourTrip, id=id)
    print(trip01, '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^6')
    context = {
        'trip01': trip01
    }
    return render(request, 'triper.html', context)


def single(request, id):
    print(id, '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    blog01 = get_object_or_404(YourStory, id=id)
    print(blog01, '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^6')
    context = {
        'blog01': blog01
    }
    return render(request, 'single.html', context)


def contact(request):
    return render(request, 'contact.html', locals())


def register(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        print(form)
        if form.is_valid():
            print("---------------------------------------------the bitches-------------------------------------")
            print("form is valid")
            password = form.cleaned_data.get('password')
            password2 = form.cleaned_data.get('password2')
            if password == password2:
                form.save()
                print("---------------------------------------------the boys-------------------------------------")
                return redirect('option')
            messages.info(request, 'pass is not same')
            return redirect('register')
        else:
            messages.info(request, 'error in form')
            return redirect('register')
    else:
        form = ProfileForm()
    return render(request, 'register.html', locals())


def log_in(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            print("form is valid")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            print(user, "-----------------------usr")
            if user is not None:
                login(request, user)
                return redirect('option')
                messages.success(request, "Login successful")
            else:
                form.add_error('username', 'Invalid login credentials')
                messages.error(request, "Invalid username or password")
                messages.error(request, "Do you have an account? If not Register!")
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


def addstory(request):
    if request.method == 'POST':
        form = AddYourStory(request.POST, request.FILES)
        print(form)
        print('---------------------------------------the cows-------------------------------------------')
        if form.is_valid():
            form.save()
            print('---------------------------------------the dogs-------------------------------------------')
            messages.info(request, 'your story has been posted!!')
            return redirect('home')
        else:
            print('---------------------------------------the cats-------------------------------------------')
            return redirect('addstory')
    else:
        form = AddYourStory()
        print(form,'*********************************************************************')
    return render(request, 'addstory.html', {'form': form})


def addtrip(request):
    if request.method == 'POST':
        form = AddYourTrip(request.POST, request.FILES)
        print(form)
        print('---------------------------------------the cows-------------------------------------------')
        if form.is_valid():
            form.save()
            print('---------------------------------------the dogs-------------------------------------------')
            messages.info(request, 'your story has been posted!!')
            return redirect('home')
        else:
            print('---------------------------------------the cats-------------------------------------------')
            return redirect('addtrip')
    else:
        form = AddYourTrip()
        print(form,'*********************************************************************')
    return render(request, 'addtrip.html', {'form': form})


def contact(request, first_name=None, last_name=None, ):
    if request.method == "POST":
        form = ContactForm(request.POST)
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        if form.is_valid():
            email = request.POST.get("email")
            form.save()
            print('???????????????????????????????????????/')
            saved = True
            messages.success(request, 'Thank-you for Contacting Us')
            print(email, "---------------email")
            d = ({'email': email})
            plaintext = get_template('email.txt')
            subject, from_email, to = 'Thank You For Contacting Us', 'care@clindle.com', email
            text_content = plaintext.render(d)
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.send()
            thankyou = True
        else:
            messages.error(request, 'Your Information  Was Not  Update')
    else:
        form = ContactForm()
    return render(request, 'contact.html', locals())


