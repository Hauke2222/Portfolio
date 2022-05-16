from django.shortcuts import get_list_or_404, get_object_or_404, render
from .models import Project

# Create your views here.


def index(request):
    projects = get_list_or_404(Project.objects.all().order_by("-date"))
    return render(request, "projects/index.html", {"projects": projects})


def detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, "projects/detail.html", {"project": project})
