from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from django.core.paginator import Paginator
from .forms import StudentForm
from django.contrib.auth.decorators import login_required


def dashboard(request):
    """
    Dashboard view showing statistics and recent activity.
    """
    total_students = Student.objects.all().count()
    recent_students = Student.objects.all().order_by('-id')[:5]
    context = {
        'total_students': total_students,
        'recent_students': recent_students,
    }
    return render(request, 'students/dashboard.html', context)



def home(request):
    """
    List view with search and pagination.
    """
    query = request.GET.get('search')

    if query:
        student_list = Student.objects.filter(name__icontains=query)
    else:
        student_list = Student.objects.all()

    paginator = Paginator(student_list, 5)   # 1 page me 5 students

    page_number = request.GET.get('page')
    students = paginator.get_page(page_number)

    return render(request, 'students/home.html', {'students': students})


@login_required
def add_student(request):
    """
    View to add a new student.
    """
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = StudentForm()
    return render(request, 'students/add_student.html', {'form': form})


@login_required
def update_student(request, student_id):
    """
    View to update an existing student.
    """
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/update_student.html', {'form': form, 'student': student})


@login_required
def delete_student(request, student_id):
    """
    View to delete a student.
    """
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect('/')
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login

def signup(request):
    """
    View to handle user registration.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
