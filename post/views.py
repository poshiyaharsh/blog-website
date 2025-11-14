from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Comment

@login_required
def create_post(request):
    if request.method == "POST":
        postname = request.POST.get("postname")
        content = request.POST.get("content")
        category = request.POST.get("category")
        image = request.FILES.get("image")
        Post.objects.create(postname=postname, content=content, category=category, image=image, user=request.user)
        return redirect("blogapp:index")
    return render(request, "create.html")