from django.urls import path
from . import views

app_name = "post"

urlpatterns = [
    path("create/", views.create_post, name="create"),
    # path("edit/<int:id>/", views.edit_post, name="edit"),
    # path("delete/<int:id>/", views.delete_post, name="delete"),
    # path("increase_like/<int:id>/", views.increase_likes, name="increase_likes"),
    # path("comment/save/<int:id>/", views.save_comment, name="save_comment"),
    # path("comment/delete/<int:id>/", views.delete_comment, name="delete_comment"),
]
