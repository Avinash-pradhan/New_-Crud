from django.shortcuts import render, redirect
from myapp.models import Student
from django.db.models import Q
from django.db.models import Count

# Create your views here.

def home(request):
    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})

def add(request):
    if request.method == 'POST':
        student = request.POST['student']
        number = request.POST['number']
        email = request.POST['email']
        degree = request.POST['degree']
        yop = request.POST['yop']

        Student.objects.create(student=student, number=number, email=email, degree=degree, yop=yop)
        return redirect('home')
    return render(request, 'add.html')

def update(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.student = request.POST['student']
        student.number = request.POST['number']
        student.email = request.POST['email']
        student.degree = request.POST['degree']
        student.yop = request.POST['yop']
        student.save()
        return redirect('home')
    return render(request, 'update.html', {'student': student})

def delete(request, id):
    if request.method == 'POST':
        try:
            student = Student.objects.get(id=id)
            student.delete()
        except Student.DoesNotExist:
            # Optionally handle the case where the student doesn't exist
            pass
    return redirect('home')
