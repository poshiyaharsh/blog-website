from django.shortcuts import render, get_object_or_404
from django.conf import settings
from post.models import Post, Comment

def index(request):
    posts = Post.objects.filter(user_id=getattr(request.user, "id", None)).order_by("-id")
    top_posts = Post.objects.all().order_by("-likes")[:5]
    recent_posts = Post.objects.all().order_by("-id")[:5]
    return render(request, "index.html", {
        "posts": posts,
        "top_posts": top_posts,
        "recent_posts": recent_posts,
        "user": request.user,
        "media_url": settings.MEDIA_URL,
    })

def blog(request):
    posts = Post.objects.filter(user_id=getattr(request.user, "id", None)).order_by("-id")
    return render(request, "blog.html", {
        "posts": posts,
        "top_posts": Post.objects.all().order_by("-likes"),
        "recent_posts": Post.objects.all().order_by("-id"),
        "user": request.user,
        "media_url": settings.MEDIA_URL,
    })

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    comments = Comment.objects.filter(post=post).order_by("-id")
    return render(request, "post-details.html", {
        "post": post,
        "comments": comments,
        "total_comments": comments.count(),
        "media_url": settings.MEDIA_URL,
        "recent_posts": Post.objects.all().order_by("-id")[:5],
    })
