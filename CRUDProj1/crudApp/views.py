from django.shortcuts import render,redirect
from crudApp.models import Student
from crudApp.forms import StudentForm

 # Create your views here. 
def diplayHome(request): 
    students=Student.objects.all() 
    stu_data={'stu_info':students}
    return render(request,'htmlpages/home.html',context=stu_data)

def insertInfo(request):
    form=StudentForm
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'htmlpages/insert.html',{'form':form})

def updateInfo(request,id):
    student=Student.objects.get(id=id)
    form=StudentForm(instance=student)
    if request.method=='POST':
        form=StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'htmlpages/nupdate.html',{'form':form})

def deleteInfo(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect('/')