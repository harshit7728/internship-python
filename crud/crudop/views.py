from django.shortcuts import render, redirect
from django.template import context
from django.template.defaulttags import url
from django.urls import reverse
from django.views import View
from django.contrib import messages
from django.db.models import Q
from .models import Student


class Studentadd(View):
    template_name = 'adminlte/index.html'

    def get(self, request):
        return render(request, 'adminlte/form.html')

    def post(self, request):
        students = Student.objects.all()

        if "create" in request.POST:
            name = request.POST.get("name")
            email = request.POST.get("email")
            Student.objects.create(
                name=name,
                email=email
            )
            messages.success(request, "Student added successfully")
        context = {"students": students, }
        return render(request, self.template_name, context)


class StudentView(View):
    template_name = 'adminlte/index.html'

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

        elif "search" in request.POST:
            search_query = request.POST.get("query")
            students = Student.objects.filter(Q(name__icontains=search_query) | Q(email__icontains=search_query))

        context = {"students": students, "search_query": search_query}
        return render(request, self.template_name, context)


class datatable(View):
    template_name = 'adminlte/datatable.html'

    def get(self, request):
        students = Student.objects.all()
        context = {"students": students, }
        return render(request, self.template_name, context)


class updateview(View):
    template_name = 'adminlte/datatable.html'

    def get(self, request, id):
        student = Student.objects.get(id=id)
        context1 = {"students": student, }
        return render(request, 'adminlte/update.html', context1)

    def post(self, request, id):
        students = Student.objects.all()

        if "update" in request.POST:
            name = request.POST.get("name")
            email = request.POST.get("email")
            student = Student.objects.get(id=id)
            student.name = name
            student.email = email
            student.save()
            messages.success(request, "student updated successfully")

            context = {"students": students, }
            return render(request, self.template_name, context)
