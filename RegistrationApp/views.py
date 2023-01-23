from django.shortcuts import render,redirect
from RegistrationApp.models import Categorydb,Products,add_admindb,emailsubdb,messagedb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from Frontapp.views import homepg
# Create your views here.

def index(request):
    return render(request,'index.html')

def add_admin(request):
    return render(request,'add _admin.html')
def add_adminsave(request):
    if request.method=="POST":
        na=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        password=request.POST.get('password')
        image=request.FILES['image']
        obj=add_admindb(name=na,email=email,mobile=mobile,password=password,image=image)
        obj.save()
        return redirect(add_admin)

def fun_displayadmin(request):
    data=add_admindb.objects.all()
    return render(request,'display_admin.html',{'data':data})

def editadmin(request,dataid):
    data=add_admindb.objects.get(id=dataid)
    print(data)
    return render(request,'editadmin.html',{'data':data})

def updateadmin(request,dataid):
    if request.method == "POST":
        na = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = add_admindb.objects.get(id=dataid).image
        add_admindb.objects.filter(id=dataid).update(name=na,email=email,mobile=mobile,password=password,image=file)
        return redirect(fun_displayadmin)
def deleteadmin(request,dataid):
    data=add_admindb.objects.filter(id=dataid)
    data.delete()
    return redirect(fun_displayadmin)


def add_category(request):

    return render(request,'add_category.html')
def add_categorysave(request):
    if request.method=="POST":
        na=request.POST.get('name')
        ds=request.POST.get('discription')
        image=request.FILES['image']
        obj=Categorydb(Name=na, Description=ds, Image=image)
        obj.save()
    return redirect(add_category)
def fun_display(request):
    data=Categorydb.objects.all()
    return render(request,'displaycategory.html',{'data':data })
def editcategory(request,dataid):
    data=Categorydb.objects.get(id=dataid)
    print(data)
    return render(request,'editcategory.html',{'data':data})
def updatecategory(request,dataid):
    if request.method=="POST":
        na = request.POST.get('name')
        ds = request.POST.get('discription')
        try:
            img=request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=Categorydb.objects.get(id=dataid).Image
        Categorydb.objects.filter(id=dataid).update(Name=na, Description=ds, Image=file)
        return redirect(fun_display)
def deletecategory(request,dataid):
    data=Categorydb.objects.filter(id=dataid)
    data.delete()
    return redirect(fun_display)




def add_book(request):
    data=Categorydb.objects.all()
    return render(request,'add_books.html',{'data':data})
def add_booksave(request):
    if request.method=="POST":
        ca=request.POST.get('category')
        na=request.POST.get('name')
        pd=request.POST.get('publish_date')
        an=request.POST.get('author_name')
        pr=request.POST.get('price')
        image=request.FILES['image']
        obj1=Products( Name=na,Price=pr, Published_Date=pd, author_name=an, Categry=ca, Image=image)
        obj1.save()
        return redirect(add_book)
def fun_displaybook(request):
    data=Products.objects.all()
    return render(request,'Display_book.html',{'data':data})
def editbook(request,dataid):
    dat=Categorydb.objects.all()
    data=Products.objects.get(id=dataid)
    print(data)
    return render(request,'editbook.html',{'data':data,'dat':dat})
def updatebook(request,dataid):
    if request.method=="POST":
        ca=request.POST.get('category')
        na=request.POST.get('name')
        pd=request.POST.get('publish_date')
        an=request.POST.get('author_name')
        pr=request.POST.get('price')
        try:
            img=request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=Products.objects.get(id=dataid).Image
        Products.objects.filter(id=dataid).update( Name=na, Published_Date=pd, author_name=an, Price=pr,Categry=ca, Image=file)
        return redirect(fun_displaybook)
def deletebook(request,dataid):
    data=Products.objects.filter(id=dataid)
    data.delete()
    return redirect(fun_displaybook)

def adminloginpg(request):
    return render(request,'adminloginpgg.html')
def adminloginfun(request):
    if request.method=="POST":
        un=request.POST.get('username')
        ps=request.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            user = authenticate(username=un, password=ps)
            if user is not None:
                login(request,user)
                request.session['username'] = un
                request.session['password'] = ps
                return redirect(index)
            else:
                return redirect(adminloginpg)
        else:
            return redirect(adminloginpg)

def emaildbfun(request):
    if request.method=="POST":
        em=request.POST.get('email')
        obj=emailsubdb(email=em)
        obj.save()
    return redirect(homepg)

def mssg(request):
    data=messagedb.objects.all()
    return render(request,'messagedisplay.html',{'data':data})


