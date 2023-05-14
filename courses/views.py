from django.shortcuts import render
from .models import Courses

# Create your views here.


def courses(request):
    context = {}
    context["dataset"] = Courses.objects.all()
    return render(request, 'index_courses.html', context)
