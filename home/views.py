from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout

# Create your views here.
def index(request):
    return render(request,"index.html")

    # context={
    #     "variable" : "Sid is great"
    # }

    # in html file for creating variable
    # variable value is {{variable}}
    # return render(request,"index.html", context)
    # return HttpResponse("This is home page")
    
def about(request):
    return render(request,"about.html")

    # return HttpResponse("This is about page")
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, age=age,desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your Form Successfully Submitted")
    return render(request,"contact.html")

    # return HttpResponse("This is contact page")
def classes(request):
    return render(request,"class.html")

    # return HttpResponse("This is classes page")

def handleSignUp(request):
    if request.method == "POST":
        # Get the post parameter
        username = request.POST.get('username')
        useremail = request.POST.get('useremail')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if not username.isalnum():
            messages.error(
                request, " User name should only contain letters and numbers")
            return redirect('/')
        if (pass1 != pass2):
            messages.error(request, " Passwords do not match")
            return redirect('/')

        # create the user
        myuser = User.objects.create_user(username, useremail, pass1)
        myuser.save()
        messages.success(request, 'Your Account Has been Craeted successfully')
        return redirect('/')

    else:
        return HttpResponse('404 Not Found')


def handeLogin(request):
    if request.method == "POST":
        # Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/")

    return HttpResponse("404- Not found")

    return HttpResponse("login")



def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')