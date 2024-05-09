from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from contactenquiry.models import ContactEnquiry


def homepage(request):
   
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def calculator(request):
    c=''
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            opr=request.POST.get('opr')
            if opr=='+':
                c=n1+n2
            elif opr=='-':
                c=n1-n2
            elif opr=='*':
                c=n1*n2
            elif opr=='/':
                c=n1/n2
            

    except:
        c="Invalid operation"
    print(c)
    return render(request,"calculator.html",{'c':c})

def contact(request):
    final=0
    
    try:
        if request.method=="POST":    
        
        # n1=int(request.Get['num1'])
        # n2=int(request.Get['num2'])
            n1=int(request.Get.get('num1'))
            n2=int(request.Get.get('num2'))
            final=n1+n2

            return HttpResponseRedirect('thank/')
    except:
        pass
    return render(request,"contact.html",{'output':final})

def service(request):
    return render(request,"service.html")
def saveenquiry(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        msg=request.POST.get('msg')
        en=ContactEnquiry(name=name,email=email,phone=phone,msg=msg)
        en.save()
    
    return render(request,"contact.html")

def marksheet(request):
    if request.method=="POST":
        n1=eval(request.POST.get('num1'))
        n2=eval(request.POST.get('num2'))
        n3=eval(request.POST.get('num3'))
        n4=eval(request.POST.get('num4'))
        n5=eval(request.POST.get('num5'))
        t=n1+n2+n3+n4+n5
        p=t*100/500;
        if p>=70:
            d="First div"
        elif p>=50:
            d="Second div"
        elif p>=33:
            d="Third div"
        else:
            d="Failed "
        
        data={
            'total':t,
            'per':p,
            'div':d
        }
        
        return render(request,"marksheet.html",data)
        
    return render(request,"marksheet.html")

def evenodd(request):

    c=''
    if request.method=="POST":
         if request.POST.get("num1")=="":
            return render(request,"evenodd.html",{'error':True})
    if request.method=="POST":
         if request.POST.get("num1")=="#":
            return render(request,"evenodd.html",{'error':True})

    if request.method=="POST":

        n=eval(request.POST.get('num1'))
        if n%2==0:
            c="Even Number"
        else:
            c="Odd Number"

    return render(request,"evenodd.html",{'c':c})

def coursedetails(request,courseid):
    return HttpResponse(courseid)

def form(request):
    final=0
    try:
        if request.method=="POST":
        # n1=int(request.GET['numA'])
        # n2=int(request.GET['numB'])
           n1=int(request.POST.get('numA'))
           n2=int(request.POST.get('numB'))
           final=(n1+n2)
    except:
        pass
    return render(request,"form.html",{'output':final})

def thank(request):
    return render(request,"thank.html")