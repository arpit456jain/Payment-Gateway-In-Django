from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
import razorpay
from yogaClasses.settings import ROZARPAY_API_KEY,ROZARPAY_SECRET_KEY
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

# from django.contrib import messages

def home(request):
    if request.user.is_authenticated:
        return render(request,'index.html')
    else:
        # messages.success(request, "Your message has been successfully sent")
        return redirect('/')
def dashboard(request):
    return render(request,'dashboard.html')


def makePayment(request):
    if request.method == 'POST':    
        amount = 500*100
        client = razorpay.Client(
            auth=(ROZARPAY_API_KEY,ROZARPAY_SECRET_KEY))
        payment = client.order.create({'amount':amount, 'currency':'INR', 'payment_capture':'1'})
        # print(payment)
     
        params = {'api_key':ROZARPAY_API_KEY,'payment' : payment}
        # print(amount)
        return render(request,'makePayment.html',params)
     
    return render(request,'makePayment.html')

@csrf_exempt
def success(request):
    if request.method == "POST":
       return render(request,'success.html')


def signup(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            firstname = request.POST['firstname']
            password = request.POST['password']
            email = request.POST['email']
            age = request.POST['age']
            batch = request.POST['batch']
            print(username, password,email,batch,firstname)
            user = user = User.objects.create_user(username, email, password,age)
            user.save()
            return redirect('/makePayment')
        except Exception as e:
           return HttpResponse("error occured"+str(e))
    else:
        print("get")
        
    return render(request, 'signup.html')

def loginuser(request):
    if request.user.is_authenticated:
        return redirect('/home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("login")
            # Redirect to a success page.
            return redirect('/home')
        else:
            print("invalid")
    return render(request, 'login.html')

def logoutuser(request):
    logout(request)
    return redirect('/')
