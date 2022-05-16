from django.shortcuts import get_list_or_404, get_object_or_404, render
from .models import Post, Comment

# Create your views here.


def index(request):
    posts = get_list_or_404(Post.objects.all().order_by("-date"))
    return render(request, "blog/index.html", {"posts": posts})


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/detail.html", {"post": post})
