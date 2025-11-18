from django.urls import path
from blog import views

urlpatterns = [
    path("post_list/", views.post_list, name="post_list"),
    path("<int:post_id>/", views.post_info, name="post_info"),
    path("author/<str:author_name>/", views.author_post, name="author_to_post"),
]