from django.shortcuts import render, redirect
from .forms import StudentForm
from django.contrib import messages

def enroll_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student enrolled successfully!")
            return redirect('enroll_success')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = StudentForm()
    return render(request, 'enro.html', {'form': form})

def enroll_success(request):
    return render(request, 'success.html')