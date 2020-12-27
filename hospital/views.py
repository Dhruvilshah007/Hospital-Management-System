from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from .models import *

# Create your views here.
def About(request):
    return render(request,'about.html')

def Contact(request):
    return render(request,'contact.html')

def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    
    # saving all data form each model in variables to check total in each!
    doctors=Doctor.objects.all()
    patient=Patient.objects.all()
    appointment=Appointment.objects.all()

    d=0
    p=0
    a=0
    for i in doctors:
        d+=1
    for i in patient:
        p+=1
    for i in appointment:
        a+=1
    
    d1={'d':d,'p':p,'a':a}
    return render(request,'index.html',d1)

    
def Login(request):
    error=""
    if request.method=='POST':
        u=request.POST['uname']
        p=request.POST['pwd']
        user=authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                error="no"
            else:
                error="yes"

        except:
            error="yes"
    d={'error':error}
    return render(request,'login.html',d)

def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')



# Doctor

def View_Doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc=Doctor.objects.all()
    d={'doc':doc}
    return render(request,'view_doctor.html',d)

def Add_Doctor(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method=='POST':
        n=request.POST['name']
        c=request.POST['contact']
        sp=request.POST['special']
        try:
            Doctor.objects.create(name=n,mobile=c,special=sp)
            error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request,'add_doctor.html',d)

def Delete_Doctor(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor=Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor')
   
def edit_Doctor(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    doc=Doctor.objects.filter(id=pid)
    d={'doc':doc}
    if request.method=="POST":
        n=request.POST['name']
        c=request.POST['contact']
        sp=request.POST['special']
        doc=Doctor.objects.get(id=pid)
        doc.name=n
        doc.mobile=c
        doc.special=sp
        doc.save()
        return redirect('view_doctor')
    return render(request,'edit_doctor.html',d)

# Patient

def View_Patient(request):
    if not request.user.is_staff:
        return redirect('login')
    pat=Patient.objects.all()
    d={'pat':pat}
    return render(request,'view_patient.html',d)

def Add_Patient(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method=='POST':
        n=request.POST['name']
        g=request.POST['gender']
        c=request.POST['mobile']
        a=request.POST['address']
        try:
            Patient.objects.create(name=n,gender=g,mobile=c,address=a)
            error="no"
        except:
            error="yes"
    d={'error':error}
    return render(request,'add_patient.html',d)

def Delete_Patient(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    patient=Patient.objects.get(id=pid)
    patient.delete()
    return redirect('view_patient')

def edit_Patient(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    doc=Patient.objects.filter(id=pid)
    d={'doc':doc}
    if request.method=="POST":
        n=request.POST['name']
        g=request.POST['gender']
        c=request.POST['mobile']
        a=request.POST['address']
        doc=Patient.objects.get(id=pid)
        doc.name=n
        doc.gender=g
        doc.mobile=c
        doc.address=a
        doc.save()
        return redirect('view_patient')
    return render(request,'edit_patient.html',d)


# appointment
def View_Appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    appoint=Appointment.objects.all()
    d={'appoint':appoint}
    return render(request,'view_appointment.html',d)

def Add_Appointment(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    # collecting data in a variable 
    doctor1=Doctor.objects.all()
    patient1=Patient.objects.all()
    if request.method=='POST':
        d=request.POST['doctor']
        p=request.POST['patient']
        d1=request.POST['date']
        t1=request.POST['time']
        doctor=Doctor.objects.filter(name=d).first()
        patient=Patient.objects.filter(name=p).first()
        
        try:
            Appointment.objects.create(doctor=doctor,patient=patient,date1=d1,time1=t1)
            error="no"
        except:
            error="yes"
    d={'doctor':doctor1,'patient':patient1,'error':error}
    return render(request,'add_appointment.html',d)

def Delete_Appointment(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    appointment=Appointment.objects.get(id=pid)
    appointment.delete()
    return redirect('view_appointment')

def edit_Appointment(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    doc=Appointment.objects.filter(id=pid)
    doctor1=Doctor.objects.all()
    patient1=Patient.objects.all()
    if request.method=='POST':
        d=request.POST['doctor']
        p=request.POST['patient']
        d1=request.POST['date']
        t1=request.POST['time']
        doctor=Doctor.objects.filter(name=d).first()
        patient=Patient.objects.filter(name=p).first()

        doc=Appointment.objects.get(id=pid)
        doc.date1=d1
        doc.time1=t1
        
        
        
    d={'doctor':doctor1,'patient':patient1,'doc':doc}

    return render(request,'edit_appointment.html',d)