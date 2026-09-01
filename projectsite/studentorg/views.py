from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from studentorg.models import Organization, OrgMember, Student, College
from studentorg.forms import OrganizationForm, OrganizationMemberForm, StudentForm, CollegeForm
from django.urls import reverse_lazy

class HomePageView(ListView):
    model = Organization
    context_object_name = "home"
    template_name = "home.html"

class OrganizationList(ListView):
    model = Organization
    context_object_name = "organization"
    template_name = "org_list.html"
    paginate_by = 5

class OrganizationMemberListView(ListView):
    model = OrgMember
    context_object_name = "organization_member"
    template_name = "orgmem_list.html"
    paginate_by = 5

class StudentListView(ListView):
    model = Student
    context_object_name = "student"
    template_name = "stu_list.html"
    paginate_by = 5


class CollegeListView(ListView):
    model = College
    context_object_name = "college"
    template_name = "college_list.html"
    paginate_by = 5

class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = "org_form.html"
    success_url = reverse_lazy("organization-list")

class OrganizationMemberCreateView(CreateView):
    model = OrgMember
    form_class = OrganizationMemberForm
    template_name = "orgmem_form.html"
    success_url = reverse_lazy("organization-member-list")

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = "stu_form.html"
    success_url = reverse_lazy("student-list")


class CollegeCreateView(CreateView):
    model = College
    form_class = CollegeForm
    template_name = "college_form.html"
    success_url = reverse_lazy("college-list")

class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = "org_form.html"
    success_url = reverse_lazy("organization-list")

class OrganizationMemberUpdateView(UpdateView):
    model = OrgMember
    form_class = OrganizationMemberForm
    template_name = "orgmem_form.html"
    success_url = reverse_lazy("organization-member-list")

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "stu_form.html"
    success_url = reverse_lazy("student-list")


class CollegeUpdateView(UpdateView):
    model = College
    form_class = CollegeForm
    template_name = "college_form.html"
    success_url = reverse_lazy("college-list")

class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = "org_del.html"
    success_url = reverse_lazy("organization-list")

class OrganizationMemberDeleteView(DeleteView):
    model = OrgMember
    template_name = "orgmem_del.html"
    success_url = reverse_lazy("organization-member-list")

class StudentDeleteView(DeleteView):
    model = Student
    template_name = "stu_del.html"
    success_url = reverse_lazy("student-list")

class CollegeDeleteView(DeleteView):
    model = College
    template_name = "college_del.html"
    success_url = reverse_lazy("college-list")