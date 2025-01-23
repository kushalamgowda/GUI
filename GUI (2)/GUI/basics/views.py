from django.shortcuts import render
from .models import *
from django.shortcuts import redirect

# Create your views here.
def aboutus(request):
    return render(request,'aboutus.html')
def index(request):
    return render(request,'index.html')

def counter(request):
    if(request.method=="POST"):
        data=request.POST
        result=data.get('textresult')
        if result=="":
            result=0
        else:
            result=int(data.get('textresult'))
        if('buttonincrement' in request.POST):
            result=result+1
            return render(request,'counter.html',context={'result':result})
        if('buttondecrement' in request.POST):
            result=result-1
            return render(request,'counter.html',context={'result':result})
        if('buttonreset' in request.POST):
            result=0
            return render(request,'counter.html',context={'result':result})

    return render(request,'counter.html')


def register(request):
    if(request.method=="POST"):
        data=request.POST
        firstname=data.get('textfirstname')
        lastname=data.get('textlastname')
        if('buttonsubmit' in request.POST):
            result=firstname+" "+lastname
            return render(request,'register.html',context={'result':result})

    return render(request,'register.html')

def calci(request):
    if(request.method=="POST"):
        data=request.POST
        firstnumber=int(data.get('textfirstnumber'))
        secondnumber=int(data.get('textsecondnumber'))
        print(firstnumber)
        print(secondnumber)
        if('buttonadd' in request.POST):
            result=firstnumber+secondnumber
            return render(request,'calci.html',context={'result':"Sum="+str(result)})
        if('buttonsub' in request.POST):
            result=firstnumber-secondnumber
            return render(request,'calci.html',context={'result':"Sub="+str(result)})
        if('buttonmul' in request.POST):
            result=firstnumber*secondnumber
            return render(request,'calci.html',context={'result':"Mul="+str(result)})
        if('buttondiv' in request.POST):
            result=firstnumber/secondnumber
            return render(request,'calci.html',context={'result':"Div="+str(result)})
        

    return render(request,'calci.html')

def department(request):
    if(request.method=="POST"):
        data=request.POST
        deptname=data.get('textdepartmentname')
        deptdesc=data.get('textdepartmentdesc')
        StudentDepartment.objects.create(DEPT_NAME=deptname,DEPT_DESC=deptdesc)
        result="Department Details saved Succefully"
        return render(request,'department.html',context={'result':result})


    return render(request,'department.html')
def departmentview(request):
    getdepartment=StudentDepartment.objects.all()
    return render(request,'departmentview.html',context={'getdepartment':getdepartment})

def departmentupdate(request,id):
  getdepartments=StudentDepartment.objects.get(id=id)
  if(request.method=="POST"):
    data=request.POST
    deptname=data.get('textdepartmentname')
    deptdesc=data.get('textdepartmentdesc')
    getdepartments.DEPT_NAME=deptname
    getdepartments.DEPT_DESC=deptdesc
    getdepartments.save()
    return redirect('/departmentview/')
  return render(request,'departmentupdate.html',context={'getdepartments':getdepartments})

def departmentdelete(request,id):
  getdepartments=StudentDepartment.objects.get(id=id)
  if(request.method=="POST"):
    data=request.POST
    getdepartments.delete()
    return redirect('/departmentview/')
  return render(request,'departmentdelete.html',context={'getdepartments':getdepartments})