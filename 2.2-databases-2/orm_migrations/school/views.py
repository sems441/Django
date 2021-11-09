from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    context = {}

    ordering = 'group'
    students_query = Student.objects.all().prefetch_related('teachers')

    context['students_query'] = students_query.order_by(ordering)
    return render(request, template, context)
