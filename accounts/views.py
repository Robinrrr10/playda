from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.
def signin(request):
    print("sign in......")
    if request.method == 'POST': 
        userName = request.POST['user_name']
        password = request.POST['passwd']
        user = auth.authenticate(username = userName, password = password)
        if user is not None:
            auth.login(request, user)
            print("user login successfull")
            return redirect('/')
        else:
            messages.info(request, "Invalid credential. Please give valid username and password")
            return redirect('login')
        
        return render(request, 'index.html')
    else:
        return render(request, 'signin.html')

def signup(request):
    print("sign up.......")
    if request.method == 'POST':
        userName = request.POST['user_name']
        firstName = request.POST['first_name']
        lastName = request.POST['last_name']
        emailId = request.POST['email_id']
        password = request.POST['password']
        confirmPassword = request.POST['confirm_password']
        if password == confirmPassword:
            if User.objects.filter(username=userName).exists() == False and User.objects.filter(username=userName).exists() == False:
                user = User.objects.create_user(username=userName, password=password, email=emailId, first_name=firstName, last_name=lastName)
                user.save()
                return redirect('/')
            else:
                messages.info(request, "User name or email already exists.")
                return redirect('signup')
        else:
            messages.info(request, "Password is not matching. Please retry...")
            return redirect('signup')
    else:
        return render(request, 'signup.html')

def signout(request):
    print("signout......")
    auth.logout(request)
    return redirect('/')