from django.urls import path
from . import views

app_name = "blogapp"

urlpatterns = [
    path("", views.index, name="index"),
    path("blog/", views.blog, name="blog"),
    path("post/<int:id>/", views.post_detail, name="post_detail"),
]
