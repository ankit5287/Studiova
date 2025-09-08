from django.shortcuts import render
from .models import User,Signup,Loign
# Create your views here.
def index(request):
    if request.method=='POST':
        User.objects.create(
            Name = request.POST['name'],
            Email = request.POST['email'],
            Description = request.POST['description']
        )
        msg = 'Details Saved Successfully'
        return render(request,'index.html',{'msg':msg})
    return render(request,'index.html')

def about(request):
    
    return render(request,'about-us.html')

def project(request):
    return render(request,'projects.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):
    if request.method=='POST':
        User.objects.create(
            Name = request.POST['name'],
            Email = request.POST['email'],
            Description = request.POST['description']
        )
        msg = 'Details Saved Successfully'
        return render(request,'contact.html',{'msg':msg})
    return render(request,'contact.html')

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()

        try:
            # case-insensitive lookup for Email
            login = Signup.objects.get(Email__iexact=email)

            if login.Password == password:
                request.session['Email'] = login.Email
                request.session['Name'] = login.Name
                return render(request, 'index.html')
            else:
                msg = 'Password is incorrect'
                return render(request, 'sign-in.html', {'msg': msg})

        except Signup.DoesNotExist:
            msg = 'Email is not registered'
            return render(request, 'sign-in.html', {'msg': msg})

    return render(request, 'sign-in.html')

def signup(request):
    if request.method == 'POST':
        try:
            Signup.objects.get(Email=request.POST['email'])
            msg = 'Email Already registerd'
            return render(request,'sign-up.html',{'msg':msg})
        except:
            Signup.objects.create(
                Name = request.POST['name'],
                Email = request.POST['email'],
                Password = request.POST['password']
            
            )
            msg = 'User Signed Up Successfully'
            return render(request,'sign-up.html',{'msg':msg})
    return render(request,'sign-up.html')

def signout(request):
    try:
         del request.session['Email']
         del request.session['Name']
         return render(request,'index.html')
    except:
      return render(request,'index.html')
