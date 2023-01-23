from django.shortcuts import render,redirect
from RegistrationApp.models import Categorydb,Products
from Frontapp.models import signupdb
from RegistrationApp.models import messagedb
from django.contrib import messages
from Frontapp.models import cartdb

# Create your views here.
def homepg(request):
    da=Categorydb.objects.all()
    return render(request,'homepage.html',{'da':da})
def aboutpg(request):
    da = Categorydb.objects.all()
    return render(request,'about.html',{'da':da})
def blogpg(reruest):
    da = Categorydb.objects.all()
    return render(reruest,'blog.html',{'da':da})
def contactpg(request):
    da = Categorydb.objects.all()
    return render(request,'contact.html',{'da':da})
def productpg(request):
    da= Categorydb.objects.all()
    data=Products.objects.all()
    return render(request,'product.html',{'data':data,'da':da})
def discat(request,itemcatg):
    da=Categorydb.objects.all()
    print("==itemcatg==",itemcatg)
    catg=itemcatg.upper()
    products=Products.objects.filter(Categry=itemcatg)
    context={
        'products':products,
        'catg':catg,
        'da':da,

    }
    return render(request,'categorydisplay.html',context)
def detailpg(request,dataid):
    da=Categorydb.objects.all()
    data=Products.objects.get(id=dataid)
    return render(request,'productdetails.html',{'data':data,'da':da})
def loginpg(request):
    da = Categorydb.objects.all()
    return render(request,'loginpg.html',{'da':da})
def signuppg(request):
    da = Categorydb.objects.all()
    return render(request,'signuppg.html',{'da':da})
def signupfun(request):
    if request.method=="POST":
        na=request.POST.get('name')
        ps=request.POST.get('password')
        cps=request.POST.get('cpassword')
        if ps==cps:
            obj=signupdb(name=na,password=ps,conformpassword=cps)
            obj.save()
            return redirect(loginpg)
        else:
            return render(request,'signuppg.html',{'msg':"Password does not matched"})

def loginfun(request):
    if request.method=="POST":
        na=request.POST.get('name')
        ps=request.POST.get('password')
        if signupdb.objects.filter(name=na,password=ps).exists():
            data=signupdb.objects.filter(name=na,password=ps).values('id').first()
            request.session['name']=na
            request.session['password']=ps
            request.session['userid']=data['id']
            return redirect(homepg)
        else:
            messages.warning(request,"Invalid username or password")
    return render(request,'loginpg.html')
def logoutfn(request):
    del request.session['name']
    del request.session['password']
    return redirect(homepg)
def mssgfun(request):
    if request.method=="POST":
        na=request.POST.get('name')
        em=request.POST.get('email')
        sub=request.POST.get('subject')
        mssg=request.POST.get('message')
        obj=messagedb(name=na,email=em,subject=sub,message=mssg)
        obj.save()
    return redirect(contactpg)
def cartpg(request):
    da = Categorydb.objects.all()
    data=cartdb.objects.all()
    return render(request,'cartpg.html',{'data':data,'da':da})
def cartdbfun(request):
    if request.method=="POST":
        na=request.POST.get('name')
        qt=request.POST.get('quantity')
        an=request.POST.get('author_name')
        to=request.POST.get('totalprice')

        obj=cartdb(Name=na, Quantity=qt, Author=an, Total=to)
        obj.save()
    return redirect(cartpg)
def deleteitem(request,dataid):

    data=cartdb.objects.filter(id=dataid)
    data.delete()
    return redirect(cartpg)
