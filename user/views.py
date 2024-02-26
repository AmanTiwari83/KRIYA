from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.
def home(request):
    rbdata=recentblog.objects.all().order_by('-id')[0:3]
    teamdata=team.objects.all().order_by('-id')[0:1]
    nevent=newevent.objects.all().order_by('-id')[0:2]
    th=thought.objects.all().order_by('-id')[0:2]
    fdata=footer.objects.all().order_by('-id')[0:1]
    md={
        "rb":rbdata,
        "team":teamdata,
        "events":nevent,
        "th":th,
        "fdata":fdata,
    }
    return  render(request,'user/home.html',md)

def index(request):
    return render(request,'user/index.html')

def register(request):
    if request.method=="POST":
        r1=request.POST.get('name')
        r2=request.POST.get('email')
        r3=request.POST.get('password')
        r4=request.POST.get('contact')
        r5=request.FILES['pic']
        r6=request.POST.get('address')
        a=registers.objects.filter(Email=r2).count()
        if a==1:
            return HttpResponse("<script>alert('You are already registered.'); location.href='/register/'</script>")
        else:
            registers(Name=r1,Email=r2,Password=r3,Contact=r4,Picture=r5,Address=r6).save()
            return HttpResponse("<script>alert('Registered Successfully.'); location.href='/register/'</script>")
    return  render(request,'user/register.html')

def signin(request):
    if request.method=="POST":
        s1=request.POST.get('username')
        s2=request.POST.get('passwd')
        b=registers.objects.filter(Email=s1,Password=s2).count()
        if b==1:
            sign(User=s1,Password=s2)
            return HttpResponse("<script>alert('Login Successfully...'); location.href='/signin/'</script>")
        else:
            return HttpResponse("<script>alert('Your userid or password is incorrect . ');  location.href='/signin/'</script>")
    return  render(request,'user/signin.html')

def contact(request):
    if request.method=="POST":
        Name=request.POST.get('name')
        Email=request.POST.get('email')
        Contact=request.POST.get('contact')
        Address=request.POST.get('add')
        Message=request.POST.get('message')
        contactus(Name=Name,Email=Email,Contact=Contact,Address=Address,Message=Message).save()
    return  render(request,'user/contact.html')

def about(request):
    adata=aboutus.objects.all().order_by('-id')[0:1]
    md={
        "adata":adata
    }
    return  render(request,'user/about.html',md)

def events(request):
    nevent=newevent.objects.all().order_by('-id')[0:20]
    md={
        "nevent":nevent
    }

    return  render(request,'user/event.html',md)

def details(request):
    eid=request.GET.get('msg')
    abc=newevent.objects.filter(id=eid)
    md={"abc":abc}
    if request.method=="POST":
        name=request.POST.get('name')
        mob=request.POST.get('mob')
        pic=request.FILES['pic']
        address=request.POST.get('address')
        gender=request.POST.get('gender')
        email=request.POST.get('email')
        date=request.POST.get('date')
        detail(name=name,mob=mob,pic=pic,address=address,gender=gender,email=email,date=date).save()
    return  render(request,'user/details.html',md)

def myprofile(request):
    return  render(request,'user/myprofile.html')