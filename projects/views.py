from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.core.paginator import Paginator
from .models import Project

# Create your views here.


def index(request):
    projects = get_list_or_404(Project.objects.all().order_by("-project_start_date"))
    paginator = Paginator(projects, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "projects/index.html", {"page_obj": page_obj})


def detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, "projects/detail.html", {"project": project})
