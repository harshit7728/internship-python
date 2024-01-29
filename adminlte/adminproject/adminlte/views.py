from django.contrib import messages
from django.shortcuts import render
from django.views import View

from .models import Student


# Create your views here.
def index(request):
    return render(request, 'adminlte/base.html')


def form(request):
    return render(request, 'adminlte/form.html')


def update(request):
    return render(request, 'adminlte/update.html')


def datatable(request):
    return render(request, 'adminlte/datatable.html')


class StudentView(View):
    template_name = 'datatable.html'

    def get(self, request):
        students = Student.objects.all()
        context = {"students": students, "search_query": ""}
        return render(request, self.template_name, context)

    def post(self, request):
        students = Student.objects.all()
        search_query = ""

        if "create" in request.POST:
            name = request.POST.get("name")
            email = request.POST.get("email")
            Student.objects.create(
                name=name,
                email=email
            )
            messages.success(request, "Student added successfully")

        elif "update" in request.POST:
            id = request.POST.get("id")
            name = request.POST.get("name")
            email = request.POST.get("email")
            student = Student.objects.get(id=id)
            student.name = name
            student.email = email
            student.save()
            messages.success(request, "student updated successfully")

        elif "delete" in request.POST:
            id = request.POST.get("id")
            Student.objects.get(id=id).delete()
            messages.success(request, "student deleted successfully")

        context = {"students": students, }
        return render(request, self.template_name, context)
